#文件操作

'''
Python 使用 open() 函数创建或打开文件，语法格式如下所示：

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

参数说明如下所示：

    file：表示将要打开的文件的路径，也可以是要被封装的整数类型文件描述符。

    mode：是一个可选字符串，用于指定打开文件的模式，默认值是 'r'（以文本模式打开并读取）。可选模式如下：

模式	描述
r	读取（默认）
w	写入，并先截断文件
x	排它性创建，如果文件已存在则失败
a	写入，如果文件存在则在末尾追加
b	二进制模式
t	文本模式（默认）
+	更新磁盘文件（读取并写入）

    buffering：是一个可选的整数，用于设置缓冲策略。

    encoding：用于解码或编码文件的编码的名称。

    errors：是一个可选的字符串，用于指定如何处理编码和解码错误（不能在二进制模式下使用）。

    newline：区分换行符。

    closefd：如果 closefd 为 False 并且给出了文件描述符而不是文件名，那么当文件关闭时，底层文件描述符将保持打开状态；
    如果给出文件名，closefd 为 True （默认值），否则将引发错误。

    opener：可以通过传递可调用的 opener 来使用自定义开启器。
'''

#creat or open a file
open('test.txt', mode='w',encoding='utf-8')

#write a file
wf = open('test.txt', 'w', encoding='utf-8')
wf.write('Tom\n')
wf.writelines(['Hello\n', 'Python'])

#close the file
wf.close()

#read the file
'''
read(size)	读取指定的字节数，参数可选，无参或参数为负时读取所有
readline()	读取一行
readlines()	读取所有行并返回列表
'''
with open('test.txt', 'r', encoding='utf-8') as rf:
    print('readline-->', rf.readline())
    print('read-->', rf.read(6))
    print('readlines-->', rf.readlines())

#positioning the file
with open('test.txt', 'rb+') as f:
    f.write(b'123456789')
    # 文件对象位置
    print(f.tell())
    # 移动到文件的第四个字节
    f.seek(3)
    # 读取一个字节，文件对象向后移动一位
    print(f.read(1))
    print(f.tell())
    # 移动到倒数第二个字节
    f.seek(-2, 2)
    print(f.tell())
    print(f.read(1))

'''
tell()	返回文件对象在文件中的当前位置
file.seek(offset[, whence])	将文件对象移动到指定的位置；offset 表示移动的偏移量；whence 为可选参数，
值为 0 表示从文件开头起算（默认值）、值为 1 表示使用当前文件位置、值为 2 表示使用文件末尾作为参考点
'''
#others
with open('test.txt', 'r+') as f:
    # 检测文件对象是否连接到终端设备
    print(f.isatty())
    # 截取两个字节
    f.truncate(2)
    print(f.read())
