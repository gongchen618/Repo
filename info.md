
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
获取特定元素
```
/dev[@id=""]
```

## 阻塞..

登录和不登录的 xpath 路径有差异，显示的信息构造可能也有差异

中文乱码处理，最后直接在最初采取 utf-8 编码解决

审查元素与查看网页源代码有区别

```
//*[@id="' + id_query + '"]/div...      RIGHT
//*[@id=' + id_query + ']/div...        WRONG
//*[@id=id_query]/div...        WRONG
```

json 似乎会把格式化内容里的字符串的换行不转义，没找到解决方案。最后是把每行分别加到了 List 里，并且在 json 格式化的时候设置 ensure_ascii = False

一定要看清楚，是父节点还是同级节点

一段废掉的代码，注意，如果想写特判，一定做好再没有其他特判的调查

```
        # 发现可能里面还有在 p 下一个层次的超链接文本，特判了一下，不知道还有没有别的
        xpath_text = xpath_query[index_query].xpath('./a/text()')
        for index_text in range(len(xpath_text)):
            context_query.append(str(xpath_text[index_text]))
        """
```

遇事不决，直接上 text

正则表达式，yyds!

class 函数没写初始化然后奇怪的没有清空新建实体？好奇怪