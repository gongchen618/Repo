#!/usr/bin/python3

from lxml import etree
import os
import json
from typing import Dict, List
import requests
from bs4 import BeautifulSoup
import lxml
import repo
import time

os.environ["http_proxy"] = "http://127.0.0.1:8889"
os.environ["https_proxy"] = "http://127.0.0.1:8889"

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"}
page_url = '/orgs/apache/repositories'

cnt = 1
while cnt < 80:
    response = requests.get("https://github.com" + page_url, headers=headers)
    response.encoding = response.apparent_encoding
    selector = etree.HTML(response.text)
    cnt = cnt + 1

# 获取仓库名字和路径
    info = selector.xpath(
        '//*[@id="org-repositories"]/div/div/div[1]/ul/li/div/div[1]/div[1]/h3/a')

# 获取下一页链接
    info = selector.xpath(
        '//*[@id = "org-repositories"]/div/div/div[3]/div/a')
    if len(info) == 1 and info[0].attrib["rel"] == "prev":
        break
    if info[0].attrib["rel"] == "next":
        page_url = info[0].attrib["href"]
    else:
        page_url = info[1].attrib["href"]
