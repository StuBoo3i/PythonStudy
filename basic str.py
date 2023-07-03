#string

#访问字符
s = 'string'
print(s[2],s[1:3],s[:4],s[3:])

#使用 ord() 函数返回单个字符的编码，chr() 函数把编码转成相应字符
x='A'
print(ord(x),chr(ord(x)))

"""
\b	退格（Backspace）
\000	空
\n	换行
\v	纵向制表符
\t	横向制表符
\r	回车
\	在行尾使用时，用作续行符
"""

s1 = 'Hello'
s2 = 'Python'
print('s1 + s2 -->', s1 + s2)
print('s1 * 4 -->', s1 * 4)
print('"H" in s1 -->','H' in s1)
print('"H" not in s1 -->','H' not in s1)
print('\\r -->', R'\r')

#  %s 格式化字符串   %d 格式化整数    %f 格式化浮点数
print('%s'%110)
print('%d'%123.112)
print('%f'%110)
#用传入的参数依次替换字符串内的占位符{0}、{1} ...
print('{0} {1}'.format('Hello', 'Python'))


