# 正则表达式
# python中re模块提供了正则表达式的功能，常用的有四个方法(match、search、findall)都可以用于匹配字符串
import re

'''
Python通过re模块提供对正则表达式的支持。使用re的一般步骤是先将正则表达式的字符串形式编译为Pattern实例，
然后使用Pattern实例处理文本并获得匹配结果（一个Match实例），最后使用Match实例获得信息，进行其他的操作。

# encoding: UTF-8
 
# 将正则表达式编译成Pattern对象
pattern = re.compile(r'hello')
 
# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = pattern.match('hello world!')
 
if match:
    # 使用Match获得分组信息
    print match.group()
 
### 输出 ###
# hello

re.compile(strPattern[, flag]):

这个方法是Pattern类的工厂方法，用于将字符串形式的正则表达式编译为Pattern对象。 第二个参数flag是匹配模式，
取值可以使用按位或运算符'|'表示同时生效，比如re.I | re.M。另外，你也可以在regex字符串中指定模式，
比如re.compile('pattern', re.I | re.M)与re.compile('(?im)pattern')是等价的。

可选值有：

    re.I(re.IGNORECASE): 忽略大小写（括号内是完整写法，下同）
    M(MULTILINE): 多行模式，改变'^'和'$'的行为（参见上图）
    S(DOTALL): 点任意匹配模式，改变'.'的行为
    L(LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
    U(UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
    X(VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。以下两个正则表达式是等价的：

a = re.compile(r"""\d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits""", re.X)
b = re.compile(r"\d+\.\d*")

re提供了众多模块方法用于完成正则表达式的功能。这些方法可以使用Pattern实例的相应方法替代，唯一的好处是少写一行re.compile()代码，
但同时也无法复用编译后的Pattern对象。这些方法将在Pattern类的实例方法部分一起介绍。如上面这个例子可以简写为：

m = re.match(r'hello', 'hello world!')
print m.group()

re模块还提供了一个方法escape(string)，用于将string中的正则表达式元字符如*/+/?等之前加上转义符再返回，在需要大量匹配元字符时有那么一点用。
'''
'''
正则表达式的匹配规则

1.单字符匹配
.  匹配出\n外的任意字符，几个点就匹配几个任意字符
[] 匹配括号中列举的字符，[^a]表示取反，[0-7]表示匹配范围
\d 匹配数字
\D 匹配非数字
\s 匹配空白，即空格，Tab，换行导致的空白也会匹配
\S 匹配非空白
\w 匹配单词字符，包括下划线，数字，字母
\W 匹配非单词字符

2.数量的匹配
* 匹配任意次
+ 匹配至少一次
? 匹配0或1次
{m} 匹配前一个字符m次
{m.}匹配前一个字符至少m次
{m.n}匹配前一个字符m到n次

3.匹配边界
^ 匹配以指定字符串开头
\b 匹配字母数字与非字母数字的边界，非字母数字与字母数字的边界
\B 匹配非单词边界

4.匹配分组
| 匹配左右任意一个表达式
(ab) 将括号中字符作为一个分组，()中的内容会作为一个元组字符装在元组中

'''
'''
match
匹配字符串

re.match()必须从字符串开头匹配！match方法尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。主要参数如下：

    re.match(pattern, string)
    # pattern     匹配的正则表达式
    # string      要匹配的字符串

re.match()方法返回一个匹配的对象，而不是匹配的内容。如果需要返回内容则需要调用group()。
通过调用span()可以获得匹配结果的位置。而如果从起始位置开始没有匹配成功，即便其他部分包含需要匹配的内容，re.match()也会返回None。
'''
a = re.match('test', 'testasdtest')
print(a)  # 返回一个匹配对象
print(a.group())  # 返回test，获取不到则报错
print(a.span())  # 返回匹配结果的位置，左闭右开区间
print(re.match('test', 'atestasdtest'))  # 返回None

print('----------------------------------------')
'''
Match对象是一次匹配的结果，包含了很多关于此次匹配的信息，可以使用Match提供的可读属性或方法来获取这些信息。

属性：

    string: 匹配时使用的文本。
    re: 匹配时使用的Pattern对象。
    pos: 文本中正则表达式开始搜索的索引。值与Pattern.match()和Pattern.seach()方法的同名参数相同。
    endpos: 文本中正则表达式结束搜索的索引。值与Pattern.match()和Pattern.seach()方法的同名参数相同。
    lastindex: 最后一个被捕获的分组在文本中的索引。如果没有被捕获的分组，将为None。
    lastgroup: 最后一个被捕获的分组的别名。如果这个分组没有别名或者没有被捕获的分组，将为None。

方法：

    group([group1, …]):
    获得一个或多个分组截获的字符串；指定多个参数时将以元组形式返回。group1可以使用编号也可以使用别名；编号0代表整个匹配的子串；
    不填写参数时，返回group(0)；没有截获字符串的组返回None；截获了多次的组返回最后一次截获的子串。
    groups([default]):
    以元组形式返回全部分组截获的字符串。相当于调用group(1,2,…last)。default表示没有截获字符串的组以这个值替代，默认为None。
    groupdict([default]):
    返回以有别名的组的别名为键、以该组截获的子串为值的字典，没有别名的组不包含在内。default含义同上。
    start([group]):
    返回指定的组截获的子串在string中的起始索引（子串第一个字符的索引）。group默认值为0。
    end([group]):
    返回指定的组截获的子串在string中的结束索引（子串最后一个字符的索引+1）。group默认值为0。
    span([group]):
    返回(start(group), end(group))。
    expand(template):
    将匹配到的分组代入template中然后返回。template中可以使用\id或\g<id>、\g<name>引用分组，但不能使用编号0。\id与\g<id>是等价的；
    但\10将被认为是第10个分组，如果你想表达\1之后是字符'0'，只能使用\g<1>0。

'''
m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')

print("m.string:", m.string)
print("m.re:", m.re)
print("m.pos:", m.pos)
print("m.endpos:", m.endpos)
print("m.lastindex:", m.lastindex)
print("m.lastgroup:", m.lastgroup)

print("m.group(1,2):", m.group(1, 2))
print("m.groups():", m.groups())
print("m.groupdict():", m.groupdict())
print("m.start(2):", m.start(2))
print("m.end(2):", m.end(2))
print("m.span(2):", m.span(2))
print(r"m.expand(r'\2 \1\3'):", m.expand(r'\2 \1\3'))

print('=========================================================')
# Pattern
'''
Pattern对象是一个编译好的正则表达式，通过Pattern提供的一系列方法可以对文本进行匹配查找。
Pattern不能直接实例化，必须使用re.compile()进行构造。
Pattern提供了几个可读属性用于获取表达式的相关信息：

    pattern: 编译时用的表达式字符串。
    flags: 编译时用的匹配模式。数字形式。
    groups: 表达式中分组的数量。
    groupindex: 以表达式中有别名的组的别名为键、以该组对应的编号为值的字典，没有别名的组不包含在内。

'''
import re

p = re.compile(r'(\w+) (\w+)(?P<sign>.*)', re.DOTALL)

print("p.pattern:", p.pattern)
print("p.flags:", p.flags)
print("p.groups:", p.groups)
print("p.groupindex:", p.groupindex)

print('============================================')

'''
实例方法[ | re模块方法]：

match(string[, pos[, endpos]]) | re.match(pattern, string[, flags]):
这个方法将从string的pos下标处起尝试匹配pattern；如果pattern结束时仍可匹配，则返回一个Match对象；如果匹配过程中pattern无法匹配，
或者匹配未结束就已到达endpos，则返回None。
pos和endpos的默认值分别为0和len(string)；re.match()无法指定这两个参数，参数flags用于编译pattern时指定匹配模式。
注意：这个方法并不是完全匹配。当pattern结束时若string还有剩余字符，仍然视为成功。想要完全匹配，可以在表达式末尾加上边界匹配符'$'。

'''

''''# 1...search(string[, pos[, endpos]]) | re.search(pattern, string[, flags]):'''
# 这个方法用于查找字符串中可以匹配成功的子串。从string的pos下标处起尝试匹配pattern，如果pattern结束时仍可匹配，则返回一个Match对象；
# 若无法匹配，则将pos加1后重新尝试匹配；直到pos=endpos时仍无法匹配则返回None。
# pos和endpos的默认值分别为0和len(string))；re.search()无法指定这两个参数，参数flags用于编译pattern时指定匹配模式。

# 将正则表达式编译成Pattern对象
pattern = re.compile(r'world')

# 使用search()查找匹配的子串，不存在能匹配的子串时将返回None
# 这个例子中使用match()无法成功匹配
match = pattern.search('hello world!')

if match:
    # 使用Match获得分组信息
    print(match.group())

### 输出 ###
# world


''''# 2...split(string[, maxsplit]) | re.split(pattern, string[, maxsplit]):'''
# 按照能够匹配的子串将string分割后返回列表。maxsplit用于指定最大分割次数，不指定将全部分割。

p = re.compile(r'\d+')
print(p.split('one1two2three3four4'))

### output ###
# ['one', 'two', 'three', 'four', '']


'''# 3...findall(string[, pos[, endpos]]) | re.findall(pattern, string[, flags]):'''
# 搜索string，以列表形式返回全部能匹配的子串。

p = re.compile(r'\d+')
print(p.findall('one1two2three3four4'))

### output ###
# ['1', '2', '3', '4']


'''#4...finditer(string[, pos[, endpos]]) | re.finditer(pattern, string[, flags]):'''
# 搜索string，返回一个顺序访问每一个匹配结果（Match对象）的迭代器。

p = re.compile(r'\d+')
for m in p.finditer('one1two2three3four4'):  # finditer
    print(m.group(), end=' ')

### output ###
# 1 2 3 4


'''# 5...sub(repl, string[, count]) | re.sub(pattern, repl, string[, count]):'''
# 使用repl替换string中每一个匹配的子串后返回替换后的字符串。
# 当repl是一个字符串时，可以使用\id或\g < id >、\g < name > 引用分组，但不能使用编号0。
# 当repl是一个方法时，这个方法应当只接受一个参数（Match对象），并返回一个字符串用于替换（返回的字符串中不能再引用分组）。
# count用于指定最多替换次数，不指定时全部替换。

p = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'

print(p.sub(r'\2 \1', s))


def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()


print(p.sub(func, s))

### output ###
# say i, world hello!
# I Say, Hello World!


'''# 6...subn(repl, string[, count]) | re.sub(pattern, repl, string[, count]):'''
# 返回(sub(repl, string[, count]), 替换次数)。

p = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'

print(p.subn(r'\2 \1', s))


def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()


print(p.subn(func, s))

### output ###
# ('say i, world hello!', 2)
# ('I Say, Hello World!', 2)
