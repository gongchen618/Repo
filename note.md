> 呜呜，烂尾了

```py
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

## 第一部分 使用入门

### 第一章 问答环节

- python 可以调用 C, C++ 的函数库，可以立即运行而无需编译，提供了高开发效率。但它没有将代码编译成底层的二进制代码，因此会比像 C 一样的完全编译语言慢一些。

- python: 面向对象的脚本语言，"脚本" 与 "程序" 相比较，往往倾向于描述简单的顶层代码文件(可以直接运行的模块文件往往也叫脚本)

- 使用 python 可以做些什么：系统编程，用户图形接口，Internet 编程，组件集成(黏合语言)，数据库编程，快速原型(?)，数值计算，游戏+图像+人工智能+XML+机器人

- "python 比 Java 更简单，更易于使用，因为 Java 从 C++ 这样的系统语言中继承了许多语法和复杂性"

### 第二章 python 如何运行程序

- 源代码 -> 字节码(.pyc)(不是机器的二进制代码)

- "冻结二进制文件" -> 打包

### 第三章 如何运行程序

- 命令行轻量编程: 交互提示模式，可用于测试自己的模块文件，print 无括号

- 命令行多行语句：最后要按两次 Enter，并且缩进一定要正确，这也意味着不能在交互提示模式中复制并粘贴多行代码，除非其中每条复合语句的后面都包含空格

- 输出重定向 `python test.py > test.out`

- `import` 同样意味着可以调用导入模块中的变量，这通过连接符 `.` 来实现，除此之外也可以使用 `from xx.py import xx` 使得可以直接调用目标变量 / 函数而无需连接符 

- `import` / `reload` 运行模块 vs `exec` 运行模块，前者封装但需要重载，后者无需重载但会覆盖外部变量

- 命令行的 `help()` 可以从一定程度上辅助编码...

```py3
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
```

## 第二部分 类型和运算

### 第四章 介绍 Python 对象类型

- "常量" 指其语法会生成对象的表达式

- python 是动态类型的

#### 字符串

- 数字，字符串和元组是不可变的。可以调用负数下标，如 `S[-1]` 与 `S[-1 + len(S)]` 是等价的。python 同样支持 slice 操作。字符串可以调用 `*` 做乘法。

- `dir(S)` 会列出变量 S 的所有属性(方法是函数属性，故也会列出)，`help(S.func)` 会返回 func 的详细信息。可作用于多种类型的通用型操作都是以内置函数或表达式的形式出现的 (len(x), X[0])，但是类型特定的操作是以方法调用的形式出现的 (aString.apper()) 。

- 字符串函数 `find` `replace` `split` `upper` `isalpha`，高级替代格式化操作 `'{0}, eggs, and {1}'.format ('spam', 'SPAM!')`。字符串还有一个叫模式匹配的高级东西


#### 列表

- 列表 `L = [123, 'spam', 1.23]`，可以通过 `append` 和 `pop` 自由增减，列表支持嵌套，通过 `M[1][2]` 取用元素，还可以处理列表解析，比如通过 `[row[1] + 1 for row in M if row[1] % 2 == 0]` `[M[i][i] for i in [0, 1, 2]]` `[c * 2 for c in 'spam'] = ['ss', 'pp', 'aa', 'mm']` 类似的语句对列表的列而非行进行像数据库一样的操作，更可以超出数据库，`G = (sum(row) for row in M), next(G)` `list(map(sum, M))`(将每个元素的函数返回值列表化)，也可以创建列表，集合，字典这样的东西

```py3
>>> squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
```

- 列表函数 `sort` `reverse`

#### 字典

- 字典 `D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}`，对一个新的字典的键赋值会新建该键，但直接调用则不会初始化默认值。字典也支持嵌套 `D['name']['last']`，嵌套列表的话，则可以通过 `D['job'].append('janitor')` 自由伸展。字典不是序列，它们不会按照加入或定义的顺序从左到右排序，若需要排序的话，可以把所有键提出来排序后再通过 `for` 执行 `Ks = list(D.keys()), Ks.sort(), for key in Ks: print(key, '=>', D[key])` 或者直接 `for key in sorted(D):...` 

#### 元组

- 元组 `T = (1, 2, 3, 4)`，不可变。字符串，元组和列表都是 "序列"，它们都有索引、合并以及分片这样的功能。

#### 文件

- 文件 `f = open('data.txt', 'w'), f.write(""), f.close()` 

#### 其他(核心类型)

- 集合 `S = set('spam'), S2 = {'a', 'b', 'c'}`，可调用 `&|-` 求交并差，只能包含不可变对象(可以包含元组，利用这一点可以储存日期，记录，IP 地址等东西)，可以过滤重复项(作为中转站)

- 十进制数(固定精度浮点数) `d = decimal.Decimal('3.414')`，`decimal.getcontect().prec = 4` 可以全局设定小数位数，但是注意必须得是小数才行...(不是普通浮点数！)

- 分数(有一个分子一个分母的有理数) `f = fractions.Fraction(2, 3)`，运算符合数学规律~(小数和分数之间可以转换)

- 布尔值 True, Flase

- 特殊占位符对象 None(可用于初始化名字和对象)

#### 其他(章节内容)

- 获取类型 `type`，但是是错的(?)

- "多态"意味着一个操作符的意义取决于被操作的对象。

### 第五章 数字

- 复数 `2 + -3j`，比较操作符可以连续使用，`x if y else z` 是三元选择表达式，`yeild x`，`lambda args: expression`(?)，`x / y` 是保留小数的除法，`x // y` 是整除(小心！)，在命令行输出多个值会被自动组成元组(注意到使用 print 和不使用 print 会得到不同的结果格式)，`random` 模块是实用的，`x in y` 返回布尔值

### 第六章 动态类型简介

- 初始化的时候，变量和对象是分开储存的，中间用指针相连接。变量名没有类型，但对象知道自己的类型。在很多语句中，对象的更新意味着生成了一个新的对象而不是修改了原有的老的对象。但是对于动态类型，可能会导致多个变量"更新"。当一个对象的计数器归零，它会被自动回收。

### 第七章 字符串

- `raw` 字符串 `r('123')` 关闭转义机制，但不能是单数个 `\`
