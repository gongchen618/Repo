# config with default.json

import json
import os

user = {} # maybe it should be a Upper
headers = {}

def LoadConfig(): # -> None
    """
    Load config from default.json to get infomation about "user" and "headers
    """
    global user, headers
    with open('docs/default.json', 'r') as f:
        data = json.load(f)
    user = data["User"]
    headers = data["Headers"]

def ProxyConnect() : # -> None
    """
    Proxy connect by proxy-infomation from default.json
    """
    with open('docs/default.json', 'r') as f:
        data = json.load(f)
    proxy = data["Proxy"]["address"] + ":" + data["Proxy"]["port"]
    os.environ["http_proxy"] = proxy
    os.environ["https_proxy"] = proxy