import os
import datetime

#查看当前路径
print(os.getcwd())

#返回指定目录下包含的文件和目录名列表
print(os.listdir('E:/'))

#返回路径 path 的绝对路径
print(os.path.abspath('../../PythonStudy'))

#将路径 path 拆分为目录和文件两部分，返回结果为元组类型
print(os.path.split("//test.txt"))

#将一个或多个 path（文件或目录） 进行拼接
print(os.path.join('/', '../../PythonStudy/test.txt'))

#返回 path（文件或目录）在系统中的创建时间
print(datetime.datetime.utcfromtimestamp(os.path.getctime('//test.txt')))

#返回 path（文件或目录）的最后修改时间
print(datetime.datetime.utcfromtimestamp(os.path.getmtime('//test.txt')))

#返回 path（文件或目录）的最后访问时间
print(datetime.datetime.utcfromtimestamp(os.path.getatime('//test.txt')))

#判断 path（文件或目录）是否存在，存在返回 True，否则返回 False。
print(os.path.exists('E:/tmp.txt'))

#判断 path 是否为目录。
print(os.path.isdir('E:/'))

#判断 path 是否为文件。
print(os.path.isfile('E:/tmp.txt'))

#返回 path 的大小，以字节为单位，若 path 是目录则返回 0。
print(os.path.getsize('//test.txt'))
print(os.path.getsize('E:/Data'))

#创建一个目录。
#os.mkdir('E:/test')

#创建多级目录。
#os.makedirs('E:/test/test2')

#目录 test1、test2 均不存在，此时使用 os.mkdir() 创建会报错，也就是说 os.mkdir() 创建目录时要保证末级目录之前的目录是存在的。

#将当前工作目录更改为 path。
#print(os.getcwd())
#os.chdir('/test')
#print(os.getcwd())

#调用 shell 脚本
print(os.system('ping www.baidu.com'))