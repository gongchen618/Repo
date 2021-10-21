
## 一直在搜的东西

直接得到可以看的懂的 xpath 返回内容
```
tree1 = html.tostring(info_repo[0])
tree2 = HTMLParser().unescape(tree1.decode('utf-8'))
```

```
print(info_commit[0].tag)
print(info_commit[0].attrib)
print(info_commit[0].text)
```

获取正常格式的文本
```
info_repo = selector_repo.xpath(
    '//*[@id="repo-content-pjax-container"]/div/div[2]/div[2]/div/div[1]/div/p')
about = ""
for index_repo in range(len(info_repo)):
    about += info_repo[index_repo].text.strip()
```
获取并列的组
```
//
```