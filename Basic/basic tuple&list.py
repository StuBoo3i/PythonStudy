#序列索引支持非负数和负数
str = 'Python'
print('str[0] str[-6] =', str[0], str[-6])
print('str[5] str[-1] =', str[5], str[-1])

"""
len()	计算序列的长度
max()	找出序列中的最大元素
min()	找出序列中的最小元素
list()	将序列转换为列表
str()	将序列转换为字符串
sum()	计算元素的和
sorted()	对元素进行排序
enumerate()	将序列组合为一个索引序列，多用在 for 循环中
"""

"""
Python 中没有数组，而是加入了功能更强大的列表（list），列表可以存储任何类型的数据，
同一个列表中的数据类型还可以不同；列表是序列结构，可以进行序列结构的基本操作：索引、切片、加、乘、检查成员，保存于中括号中
"""
l = [1024, 0.5, 'Python']
print(l[:2],l[2])

#add list elements
l.append('Hello')
print(l)

#delete list elements
del l[0]
print(l)

new_l = ['e','c','a','b','b','a',]
print(new_l.count('a'),new_l.index('c'))

#remove first element
new_l.remove('a')
print(new_l)

new_l.sort()
print(new_l)

lc = new_l.copy()
print(lc)

#元组（tuple）与列表类似，但元组是不可变的，可简单将其看作是不可变的列表，元组常用于保存不可修改的内容，保存于小括号中

t = (1024, 0.5, 'Python')
print('t[0] -->', t[0])
print('t[1:] -->', t[1:])

t = (1024, 0.5, 'Python')
print('t -->', t)
t = (1024, 0.5, 'Python', 'Hello')
print('t -->', t)

#元组中的元素不能被删除，我们只能删除整个元组

t = (1024, 0.5, 'Python')
print('len(t) -->', len(t))

t = ('d', 'b', 'a', 'f', 'd')
print('max(t) -->', max(t))
print('min(t) -->', min(t))

#将列表转换为元组
l = ['d', 'b', 'a', 'f', 'd']
t = tuple(l)
print('t -->', t)
