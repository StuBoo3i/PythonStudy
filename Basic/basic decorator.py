# 闭包（英语：Closure），又称词法闭包（Lexical Closure）或函数闭包（function closures），是引用了自由变量的函数。
# 这个被引用的自由变量将和这个函数一同存在，即使已经离开了创造它的环境也不例外。
# 所以，有另一种说法认为闭包是由函数和与其相关的引用环境组合而成的实体。
# 闭包在运行时可以有多个实例，不同的引用环境和相同的函数组合可以产生不同的实例
def x(id):
    def y(name):
        print('id:', id, 'name:', name)

    return y


y = x('ityard')
y('程序之间')

# 装饰器（decorator）也称装饰函数，是一种闭包的应用，
# 其主要是用于某些函数需要拓展功能，但又不希望修改原函数，它就是语法糖，使用它可以简化代码、增强其可读性，
# 当然装饰器不是必须要求被使用的，不使用也是可以的，Python 中装饰器通过 @ 符号来进行标识

'''
装饰器可以基于函数实现也可基于类实现，其使用方式基本是固定的，看一下基本步骤：

    定义装饰函数（类）

    定义业务函数

    在业务函数上添加 @装饰函数（类）名
    
'''


# 装饰函数
def funA(fun):
    def funB(*args, **kw):
        print('函数 ' + fun.__name__ + ' 开始执行')
        fun(*args, **kw)
        print('函数 ' + fun.__name__ + ' 执行完成')

    return funB


@funA
# 业务函数
def funC(name):
    print('Hello', name)


funC('Jhon')

print('------------------------------------------------------------')


# 装饰函数
def funA(flag):
    def funB(fun):
        def funC(*args, **kw):
            if flag == True:
                print('==========')
            elif flag == False:
                print('----------')
            fun(*args, **kw)

        return funC

    return funB


@funA(False)
# 业务函数
def funD(name):
    print('Hello', name)


funD('Jhon')


# 基于类实现
# Python 装饰器的 @... 相当于将被装饰的函数（业务函数）作为参数传入装饰函数（类）。

class Test(object):
    def __init__(self, func):
        print('函数名是 %s ' % func.__name__)
        self.__func = func

    def __call__(self, *args, **kwargs):
        self.__func()


@Test
def hello():
    print('Hello ...')


hello()
