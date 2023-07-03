#枚举

from enum import Enum

class WeekDay(Enum):
    Mon = 0
    Tue = 1
    Wed = 2
    Thu = 3
    Fri = 4

# 枚举成员
print(WeekDay.Mon)
# 枚举成员名称
print(WeekDay.Mon.name)
# 枚举成员值
print(WeekDay.Mon.value)


print('---------------------------------------')
# 方式 1
for day in WeekDay:
    # 枚举成员 枚举成员名称 枚举成员值
    print(day,day.name,day.value)

print('---------------------------------------')
# 方式 2
print(list(WeekDay))

print(WeekDay.Mon is WeekDay.Thu)
print(WeekDay.Mon == WeekDay.Mon)
print(WeekDay.Mon.name == WeekDay.Mon.name)
print(WeekDay.Mon.value == WeekDay.Mon.value)

# 确保枚举值唯一

#我们定义枚举时，成员名称是不可以重复的，但成员值是可以重复的，如果想要保证成员值不可重复，可以通过装饰器 @unique 来实现

from enum import Enum, unique

@unique
class WeekDay(Enum):
    Mon = 0
    kkk = 0
