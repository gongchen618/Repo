#!/usr/bin/python3
# 这是减短 main 代码长度而写的发送和收取 html 信息的模块

from lxml import etree
import os
import requests

os.environ["http_proxy"] = "http://127.0.0.1:8889"
os.environ["https_proxy"] = "http://127.0.0.1:8889"

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"}


def get_HTML(url: str):

    # 这里应该加入一个循环，page_url 每次改变
    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"
    selector = etree.HTML(response.text)

    return selector
