#!/usr/bin/python3
# 这个函数储存每个库的信息

from typing import Dict, List
import json


class Repo:  # 储存一个 repo 的信息
    def __init__(self):
        self.name: str = None
        self.url: str = None
        self.license: str = None
        self.about: str = None
        self.language: Dict = {}
        self.commit: List = []
        self.issue: List = []

    def append_commit(self, name: str, message: str, hash: str):
        self.commit.append({"name": name, "message": message, "hash": hash})

    def append_issue(self, name: str, context: List):
        self.issue.append({"name": name, "context": context})


def print_repo_json(it: Repo):  # 打印任务一要求信息的 json 格式
    print(json.dumps({
        "name": it.name,
        "license": it.license,
        "about": it.about,
        "language": it.language,
        "commit": it.commit,
        "issue": it.issue
    }, indent=4, ensure_ascii=False))


# 最开始储存所有 repo 是为了多线程写的，现在没用了，一直用一个就好
"""
id_pool: dict = {}


def get_repo(name: str) -> Repo:  # 对一个 repo 名字字符串返回它对应的 Repo
    if name in id_pool.keys():
        return id_pool[name]
    else:
        new_repo = Repo()
        id_pool[name] = new_repo
        return new_repo
"""
