#dict
#字典的内容在花括号 {} 内，键-值（key-value）之间用冒号 : 分隔，键值对之间用逗号 , 分隔

d = {'name':'小明', 'age':'18'}

# 使用 dict 函数
# 方式一
l = [('name', '小明'), ('age', 18)]
d = dict(l)
print(d)
# 方式二
e = dict(name='小明', age='18')
print(e)

d = dict(name='小明', age='18')
print(d['name'],d.get('name'),len(d))

d['age'] = 100
print(d.get('age'))

d.clear()
print(d)


print()
print()
#set
#集合（set）与字典相同均存储 key，但也只存储 key，因 key 不可重复，所以 set 的中的值不可重复，也是无序的

#集合使用花括号 {} 或者 set() 函数创建，如果创建空集合只能使用 set() 函数
s1 = {'a', 'b', 'c'}
s2 = set(['a', 'b', 'c'])
s3 = set()
print(s1,s2,s3)

s = {'a', 'a', 'b', 'c', 'c'}
print(s)

s4 = {'a', 'b', 'c'}
s4.add('d')
s4.update('e')
s4.add('a')
print(s4)

s5 = {'a', 'b', 'c'}
s5.remove('c')
print(s5)

s6 = {'a', 'b', 'c'}
s6.clear()
print(s6)

s7 = {'a', 'b', 'c'}
len(s)
print(s7)