#!/usr/bin/python3
# 这是爬虫主模块

from typing import Dict, List
import repo
import request

page_url = '/orgs/apache/repositories'
selector = request.get_HTML("https://github.com" + page_url)

# 获取仓库名字和路径
info_page = selector.xpath(
    '//*[@id="org-repositories"]/div/div/div[1]/ul/li/div/div[1]/div[1]/h3/a')

for index in range(len(info_page)):
    name: str = (info_page[index].text).replace(" ", "").replace("\n", "")
    url: str = (info_page[index].attrib["href"]).replace(" ", "")

    Repo = repo.get_repo(name)
    repo.Repo.name = name
    repo.Repo.url = url

    # 对单个仓库进行操作


# 获取下一页链接

"""info = selector.xpath(
        '//*[@id = "org-repositories"]/div/div/div[3]/div/a')
    if len(info) == 1 and info[0].attrib["rel"] == "prev":
        break
    if info[0].attrib["rel"] == "next":
        page_url = info[0].attrib["href"]
    else:
        page_url = info[1].attrib["href"]"""
