#!/usr/bin/python3

from typing import Dict, List


class Repo:  # 储存一个 repo 的信息
    name: str = None
    url: str = None
    license: str = None
    about: str = None
    language: Dict = {}
    commit: List = []
    issue: List = []


def Repo_json(it: Repo) -> Dict:  # 返回任务一要求信息的 json 格式
    return {
        "name": it.name,
        "license": it.license,
        "about": it.about,
        "language": it.language,
        "commit": it.commit,
        "issue": it.issue
    }


id_pool: dict = {}


def get_repo(name: str) -> Repo:  # 对一个 repo 名字字符串返回它对应的 Repo
    if name in id_pool.keys():
        return id_pool[name]
    else:
        new_repo = Repo()
        id_pool[name] = new_repo
        return new_repo
