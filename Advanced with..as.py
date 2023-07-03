'''
任何一门编程语言中，文件的输入输出、数据库的连接断开等，都是很常见的资源管理操作。但资源都是有限的，在写程序时，必须保证这些资源在使用过后得到释放，
不然就容易造成资源泄露，轻者使得系统处理缓慢，严重时会使系统崩溃。

例如，前面在介绍文件操作时，一直强调打开的文件最后一定要关闭，否则会程序的运行造成意想不到的隐患。但是，即便使用 close() 做好了关闭文件的操作，
如果在打开文件或文件操作过程中抛出了异常，还是无法及时关闭文件。

为了更好地避免此类问题，不同的编程语言都引入了不同的机制。在 python 中，对应的解决方式是使用 with as 语句操作上下文管理器（context manager），
它能够帮助我们自动分配并且释放资源。

简单的理解，同时包含 __enter__() 和 __exit__() 方法的对象就是上下文管理器。常见构建上下文管理器的方式有 2 种，分别是基于类实现和基于生成器实现。

with通过__enter__方法初始化，然后在__exit__中做善后以及处理异常。

所以使用with处理的对象必须有__enter__()和__exit__()这两个方法。

其中__enter__()方法在语句体（with语句包裹起来的代码块）执行之前进入运行，__exit__()方法在语句体执行完毕退出后运行。

with 语句适用于对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的“清理”操作，释放资源，比如
文件使用后自动关闭、线程中锁的自动获取和释放等。使用 with as 操作已经打开的文件对象（本身就是上下文管理器），无论期间是否抛出异常，
都能保证 with as 语句执行完毕后自动关闭已经打开的文件。

With语句的基本语法格式:

with expression [as target]：
    代码块

参数说明：

expression：是一个需要执行的表达式；

target：是一个变量或者元组，存储的是expression表达式执行返回的结果，可选参数。


with语句的工作原理：

紧跟with后面的语句会被求值，返回对象的__enter__()方法被调用，这个方法的返回值将被赋值给as关键字后面的变量，
当with后面的代码块全部被执行完之后，将调用前面返回对象的__exit__()方法。

with语句最关键的地方在于被求值对象必须有__enter__()和__exit__()这两个方法，那我们就可以通过自己实现这两方法来自定义with语句处理异常。

基于类实现上下文管理器：
'''


# encoding=utf-8

class opened(object):

    def __init__(self, filename):
        self.handle = open(filename)
        print("Resource:%s" % filename)

    def __enter__(self):
        print("[enter%s]: Allocate resource." % self.handle)
        return self.handle  # 可以返回不同的对象

    def __exit__(self, exc_type, exc_value, exc_trackback):
        print("[Exit %s]: Free resource." % self.handle)
        if exc_trackback is None:
            print("[Exit %s]:Exited without exception." % self.handle)
            self.handle.close()
        else:
            print("[Exit %s]: Exited with exception raised." % self.handle)
        return False  # 可以省略，缺省的None也是被看做是False


with opened(r'd:\\xxx.txt') as fp:
    for line in fp.readlines():
        print(line)

'''

opened中的__enter__() 返回的是自身的引用，这个引用可以赋值给 as 子句中的fp变量；

返回值的类型可以根据实际需要设置为不同的类型，不必是上下文管理器对象本身。

__exit__() 方法中对变量exc_trackback进行检测，如果不为 None，表示发生了异常，返回 False 表示需要由外部代码逻辑对异常进行处理；

如果没有发生异常，缺省的返回值为 None，在布尔环境中也是被看做 False，但是由于没有异常发生，__exit__() 的三个参数都为 None，
上下文管理代码可以检测这种情况，做正常处理。__exit__()方法的3个参数，分别代表异常的类型、值、以及堆栈信息。

基于生成器的上下文管理器

除了基于类的上下文管理器，它还可以基于生成器实现。接下来先看一个例子。比如，
我们可以使用装饰器 contextlib.contextmanager，来定义自己所需的基于生成器的上下文管理器，用以支持 with as 语句：

    from contextlib import contextmanager
     
    @contextmanager
    def file_manager(name, mode):
        try:
            f = open(name, mode)
            yield f
        finally:
            f.close()
     
    with file_manager('a.txt', 'w') as f:
        f.write('hello world')

这段代码中，函数 file_manager() 就是一个生成器，当我们执行 with as 语句时，便会打开文件，并返回文件对象 f；
当 with 语句执行完后，finally 中的关闭文件操作便会执行。另外可以看到，使用基于生成器的上下文管理器时，
不再用定义 __enter__() 和 __exit__() 方法，但需要加上装饰器 @contextmanager，这一点新手很容易疏忽。

需要强调的是，基于类的上下文管理器和基于生成器的上下文管理器，这两者在功能上是一致的。只不过，基于类的上下文管理器更加灵活，
适用于大型的系统开发，而基于生成器的上下文管理器更加方便、简洁，适用于中小型程序。但是，无论使用哪一种，
不用忘记在方法“__exit__()”或者是 finally 块中释放资源，这一点尤其重要。
'''
