#函数就是一段实现特定功能的代码，使用函数可以提高代码的重复利用率

# 空函数
def my_empty():
    pass

# 无返回值
def my_print(name):
    print('Hello', name)

# 有返回值
def my_sum(x, y):
    s = x + y
    print('s-->', s)
    return s

# 不定长参数
def my_variable(*params):
    for p in params:
        print(p)

# 匿名函数
my_sub = lambda x, y: x - y



my_empty()
my_print('Jhon')
result = my_sum(1, 2)
my_variable(1, 2, 3)
print()
print(my_sub(5, 1))