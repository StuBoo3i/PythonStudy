'''
1 命名空间
1.1 概念

命名空间（namespace）是名称到对象的映射，当前大部分命名空间都是通过 Python 字典来实现的，它的主要作用是避免项目中的名字冲突，每一个命名空间都是相对独立的，在不同的命名空间中可以同名，在相同的命名空间中不可以同名。
1.2 种类

命名空间主要有以下三种：

    内置：主要用来存放内置函数、异常等，比如：abs 函数、BaseException 异常。
    全局：指在模块中定义的名称，比如：类、函数等。
    局部：指在函数中定义的名称，比如：函数的参数、在函数中定义的变量等。

1.3 生命周期

通常在不同时刻创建的命名空间拥有不同的生命周期，看一下三种命名空间的生命周期：

    内置：在 Python 解释器启动时创建，退出时销毁。
    全局：在模块定义被读入时创建，在 Python 解释器退出时销毁。
    局部：对于类，在 Python 解释器读到类定义时创建，类定义结束后销毁；对于函数，在函数被调用时创建，函数执行完成或出现未捕获的异常时销毁。

2 作用域
2.1 概念

作用域是 Python 程序可以直接访问命名空间的文本区域（代码区域），名称的非限定引用会尝试在命名空间中查找名称，作用域是静态的，命名空间是随着解释器的执行动态产生的，因此在作用域中访问命名空间中的名字具有了动态性，即作用域被静态确定，被动态使用。
2.2 种类

Python 有如下四种作用域：

    局部：最先被搜索的最内部作用域，包含局部名称。
    嵌套：根据嵌套层次由内向外搜索，包含非全局、非局部名称。
    全局：倒数第二个被搜索，包含当前模块的全局名称。
    内建：最后被搜索，包含内置名称的命名空间。

作用域的搜索顺序通过下图直观的来看一下：

图片

Python 中会按上图所示作用域由内向外去搜索名字。

再通过具体代码来对作用域作进一步了解，如下所示：

# 全局作用域
g = 1
def outer():
    # 嵌套作用域
    e = 2
    def inner():
        # 局部作用域
        i = 3

2.3 global & nonlocal

我们先来看一下全局变量与局部变量。

    全局变量：定义在函数外部的变量。
    局部变量：定义在函数内部的变量。

全局变量可以在整个程序范围内进行访问，而局部变量只能在函数内部访问。通过具体示例看一下：

# 全局变量
d = 0
def sub(a, b):
    # d 在这为局部变量
    d = a - b
    print('函数内 : ', d)

sub(9, 1)
print('函数外 : ', d)

执行结果：

函数内 :  8
函数外 :  0

当内部作用域想要修改外部作用域的变量时，就要用到 global 和 nonlocal 关键字了，下面通过具体示例来了解一下。

如果我们想将上面示例中 sub() 函数中的 d 变量修改为全局变量，则需使用 global 关键字，示例如下所示：

# 全局变量
d = 0
def sub(a, b):
    # 使用 global 声明 d 为全局变量
    global d
    d = a - b
    print('函数内 : ', d)

sub(9, 1)
print('函数外 : ', d)

执行结果：

函数内 :  8
函数外 :  8

如果需要修改嵌套作用域中的变量，则需用到 nonlocal 关键字。

不使用 nonlocal

我们先来看一下不使用 nonlocal 关键字的执行情况，如下所示：

def outer():
    d = 1
    def inner():
        d = 2
        print('inner：', d)
    inner()
    print('outer：', d)
outer()

执行结果：

inner：2
outer：1

使用 nonlocal

再来看一下使用了 nonlocal 关键字的执行情况，如下所示：

def outer():
    d = 1
    def inner():
        nonlocal d
        d = 2
        print('inner：', d)
    inner()
    print('outer：', d)
outer()

执行结果：

inner：2
outer：2
'''