#!/usr/bin/python3
# 这是爬虫主模块

import re
from typing import Dict, List
import repo
import request
from itertools import count

page_url = '/orgs/apache/repositories'

while True:
    selector_page = request.get_HTML("https://github.com" + page_url)

    # 获取整个页面的仓库名字和路径
    xpath_page = selector_page.xpath(
        '//*[@id="org-repositories"]/div/div/div[1]/ul/li/div/div[1]/div[1]/h3/a')

    for index_page in range(len(xpath_page)):
        name: str = (xpath_page[index_page].text).strip()
        url: str = (xpath_page[index_page].attrib["href"]).strip()

        Repo = repo.Repo()
        Repo.name = name
        Repo.url = url

        # 对单个仓库进行操作
        selector_repo = request.get_HTML("https://github.com" + url)

        # 前三点写完了

        # 1,获取开源协议
        xpath_repo = selector_repo.xpath(
            '//*[@id="repo-content-pjax-container"]/div/div[2]/div[2]/div/div[1]/div/div[4]/a//text()')
        license = ""
        for index_repo in range(len(xpath_repo)):
            license += xpath_repo[index_repo].strip()
        Repo.license = license

        # 2,获取简介
        xpath_repo = selector_repo.xpath(
            '//*[@id="repo-content-pjax-container"]/div/div[2]/div[2]/div/div[1]/div/p')
        about = ""
        for index_repo in range(len(xpath_repo)):
            about += xpath_repo[index_repo].text.strip()
        Repo.about = about

        # 3,获取语言
        for i in count():
            xpath_repo = selector_repo.xpath(
                '//*[@id = "repo-content-pjax-container"]/div/div[2]/div[2]/div/div[6]/div/ul/li[' + str(i+1) + ']/a/span[1]')

            if (len(xpath_repo) == 0):
                break

            name_language = ""
            for index_repo in range(len(xpath_repo)):
                name_language += xpath_repo[index_repo].text.strip()

            xpath_repo = selector_repo.xpath(
                '//*[@id = "repo-content-pjax-container"]/div/div[2]/div[2]/div/div[6]/div/ul/li[' + str(i+1) + ']/a/span[2]')
            part_language = ""
            for index_repo in range(len(xpath_repo)):
                part_language += xpath_repo[index_repo].text.strip()

            Repo.language[name_language] = part_language

        # 4,获取近 5 次 commit 信息(这里默认查看 master 分支)
        # 存 bug：会不会有加载不完全（省略掉）的文本？
        # 存 bug：因为标题链接多样化，有可能含 commit hash 的链接不全是当前 commit？
        selector_commit = request.get_HTML(
            "https://github.com" + url + "/commits/master")
        xpath_commit = selector_commit.xpath(
            '//*[@id="repo-content-pjax-container"]/div[2]/div/div[2]/ol/li/div[1]')
        cnt_commit = min(5, len(xpath_commit))

        # 最后发现这里写的有点 bug，还是做的是
        for index_commit in range(0, cnt_commit):
            # 选取了一个比较合适的包含了所有所需信息的 xpath 路径
            xpath_name = xpath_commit[index_commit].xpath('./div/div[2]/a')
            try:
                name_commit = xpath_name[0].text
            except:
                print("STRANGE THING HAPPENS IN " + Repo.name)
                continue

            message_commit = ""
            hash_commit = ""
            xpath_message = xpath_commit[index_commit].xpath('./p//a')
            for i in range(len(xpath_message)):
                message_commit += xpath_message[i].text + " "

                url_commit = xpath_message[i].attrib["href"]
                if (hash_commit == "" or url_commit.startswith(url + "/commit/")):
                    hash_now = url_commit.split("/")[-1]
                    if len(hash_now) == 40:
                        # 检验是否存在冲突的 commit 的 hash
                        if (hash_commit != "" and hash_now != hash_commit):
                            print(
                                "<-------WARNING: This is a bug but I can't(lazy to) solve----->")
                        else:
                            hash_commit = hash_now

            Repo.append_commit(
                name_commit, message_commit.strip(), hash_commit)

        # 5,获取前五个 open 的 issue 标题与内容
        selector_issue = request.get_HTML(
            "https://github.com" + url + "/issues")
        xpath_issue = selector_issue.xpath(
            '//*[@id = "repo-content-pjax-container"]/div/div[3]/div[2]/div//*[@data-hovercard-type="issue"]')
        cnt_issue = min(5, len(xpath_issue))

        for index_issue in range(0, cnt_issue):
            id_query = xpath_issue[index_issue].attrib["href"].split("/")[-1]

            # 获取了单个 issue 的链接(保存 id)，还要点进去获取标题和内容（这里用 query 标示）
            selector_query = request.get_HTML(
                "https://github.com" + url + "/issues/" + id_query)

            xpath_query = selector_query.xpath(
                '//*[@id = "partial-discussion-header"]/div[1]/div/h1/span[1]')
            name_query = xpath_query[0].text

            # 它的问题描述文本路径包含了一个 issue 的标识数字字符串，需要先提取到 id_query 里
            xpath_query = selector_query.xpath(
                '//*[@id = "discussion_bucket"]/div/div[1]/div/div[1]/div[1]//div[@id]')
            id_query = xpath_query[0].attrib["id"]

            # 这一块还没有处理好爬下来的文本格式，写了一些针对我精心挑选对象的奇怪格式特判...总之也许比没有格式会能看一些
            # 但是命名乱七八糟的，恐怕得改改
            context_query = []
            xpath_query = selector_query.xpath(
                '//*[@id="' + id_query + '"]/div/div[2]/task-lists/table/tbody/tr[1]/td//text()[normalize-space()]')

            str_target = ""
            str_now = ""
            flag = False
            for index_query in range(len(xpath_query)):
                str_now = re.sub(
                    '\s{2,}', ' ', xpath_query[index_query].strip())
                if len(re.findall('"' or "'", str_now)) % 2 == 0:
                    if bool(re.search(r"[a-zA-Z]", str_now)) == True:
                        if flag == False:
                            str_target += str_now
                        else:
                            context_query.append(str_target)
                            str_target = str_now
                        flag = True
                    else:
                        str_target += str_now
                        if (str_now == ','):
                            context_query.append(str_target)
                            str_target = ""
                        flag = False

            if (len(str_target) > 0):
                context_query.append(str_target)
            Repo.append_issue(name_query, context_query)

        repo.print_repo_json(Repo)

# 获取下一页链接并继续循环
    xpath_page = selector_page.xpath(
        '//*[@id = "org-repositories"]/div/div/div[3]/div/a')
    if len(xpath_page) == 1 and xpath_page[0].attrib["rel"] == "prev":
        break
    if xpath_page[0].attrib["rel"] == "next":
        page_url = xpath_page[0].attrib["href"]
    else:
        page_url = xpath_page[1].attrib["href"]
