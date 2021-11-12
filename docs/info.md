1, authenticity_token 是隐藏在页面中，用于确认接收页面和发送表单的是同一人，避免跨站请求伪造 (CSRF) 的元素

这里可以利用 F12 查看目标提交表单中 authenticity_token 的字段，再在网页源代码中暴力检索找到需求地址

2, 不要用 F12 定位元素再复制浏览器提供的 xpath，自己写写 (可恶自己写舒服了几万倍)

3, 使用代理:
```py
import os

os.environ["http_proxy"] = "http://127.0.0.1:8889"
os.environ["https_proxy"] = "http://127.0.0.1:8889"
```
4, 为了模拟浏览器请求我们不能够直接 post，需要使用 request.Session() 先 get 再 post 以保存各种信息
```py
import requests
from requests.sessions import session
from lxml import etree

session = requests.Session()
response = session.get(url, headers=headers)
html = etree.HTML(response.text)
token = html.xpath("//*[@name='authenticity_token']/@value")
```
5, html 照原样输出
```py
html = etree.HTML(response.text)
result = etree.tostring(html, encoding='utf-8')   #解析对象输出代码
print(result.decode('utf-8'))
```
6, 研究了一下 dict 转 python class，最后突然发现 request 的传参好像必须得是 dict，于是弃了(以及小声说 python 的全局变量真的好难用)
```py
class User:
    # username, password
    def __init__(self, **entries):
        self.__dict__.update(entries)

with open('default.json', 'r') as f:
    data = json.load(f)
user = User(**data["User"])
```