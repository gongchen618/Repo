#!/usr/bin/python3
# 这是爬虫主模块

from typing import Dict, List
import repo
import request
from itertools import count

"""
page_url = '/orgs/apache/repositories'
selector_page = request.get_HTML("https://github.com" + page_url)

# 获取整个页面的仓库名字和路径
info_page = selector_page.xpath(
    '//*[@id="org-repositories"]/div/div/div[1]/ul/li/div/div[1]/div[1]/h3/a')

for index_page in range(len(info_page)):
    name: str = (info_page[index_page].text).strip()
    url: str = (info_page[index_page].attrib["href"]).strip()

    Repo = repo.get_repo(name)
    Repo.name = name
    Repo.url = url
"""
name = "openjpa"
url = "/apache/openjpa"
Repo = repo.get_repo(name)
Repo.name = name
Repo.url = url

# 对单个仓库进行操作
selector_repo = request.get_HTML("https://github.com" + url)

# 前三点写完了
"""
# 1,获取开源协议
info_repo = selector_repo.xpath(
    '//*[@id="repo-content-pjax-container"]/div/div[2]/div[2]/div/div[1]/div/div[3]/a//text()')
license = ""
for index_repo in range(len(info_repo)):
    license += info_repo[index_repo].strip()
Repo.license = license

# 2,获取简介
info_repo = selector_repo.xpath(
    '//*[@id="repo-content-pjax-container"]/div/div[2]/div[2]/div/div[1]/div/p')
about = ""
for index_repo in range(len(info_repo)):
    about += info_repo[index_repo].text.strip()

# 3,获取语言
for i in count():
    info_repo = selector_repo.xpath(
        '//*[@id = "repo-content-pjax-container"]/div/div[2]/div[2]/div/div[6]/div/ul/li[' + str(i+1) + ']/a/span[1]')

    if (len(info_repo) == 0):
        break

    name_language = ""
    for index_repo in range(len(info_repo)):
        name_language += info_repo[index_repo].text.strip()

    info_repo = selector_repo.xpath(
        '//*[@id = "repo-content-pjax-container"]/div/div[2]/div[2]/div/div[6]/div/ul/li[' + str(i+1) + ']/a/span[2]')
    part_language = ""
    for index_repo in range(len(info_repo)):
        part_language += info_repo[index_repo].text.strip()

    Repo.language[name_language] = part_language
"""

# 这个第四点没写完
"""
# 4,获取近 5 次 commit 信息(这里默认查看 master 分支)
selector_commit = request.get_HTML(
    "https://github.com" + url + "/commits/master")

try:
    info_commit = selector_commit.xpath(
        '//*[@id="repo-content-pjax-container"]/div[2]/div[1]/div[2]/ol/li[2]')
    print(info_commit)
    print()
    info_commit = selector_commit.xpath(
        '//*[@id="repo-content-pjax-container"]/div[2]/div[1]/div[2]/ol/li[1]')
    print(info_commit)

    commit = ""
    for index_commit in range(len(info_commit)):
        license += info_commit[index_commit].strip()
    print(commit)
    #Repo.license = license

except:
    # 有可能不足 5 个 commit(?)
"""

# 获取下一页链接并继续循环
"""info_page = selector_page.xpath(
        '//*[@id = "org-repositories"]/div/div/div[3]/div/a')
    if len(info_page) == 1 and info_page[0].attrib["rel"] == "prev":
        break
    if info_page[0].attrib["rel"] == "next":
        page_url = info_page[0].attrib["href"]
    else:
        page_url = info_page[1].attrib["href"]"""
