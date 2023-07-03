#time 模块的 struct_time 类代表一个时间对象，可以通过索引和属性名访问值
import datetime
import time
import calendar


t = time.localtime()
print('t-->', t)
print('tm_year-->', t.tm_year)
print('tm_year-->', t[0])

print('-----------------------------------')

print(time.time())
print(time.gmtime())
print(time.localtime())
print(time.asctime(time.localtime()))
print(time.tzname)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))   # strftime 使用

print('-----------------------------------')
#datatime 模块重新封装了 time 模块，提供了更多接口，变得更加直观和易于调用

print(datetime.date.today())
print(datetime.date.fromtimestamp(time.time()))
print(datetime.date.min)
print(datetime.date.max)

print('-----------------------------------')

td = datetime.date.today()
print(td.replace(year=1945, month=8, day=15))
print(td.timetuple())
print(td.weekday())
print(td.isoweekday())
print(td.isocalendar())
print(td.isoformat())

print('-----------------------------------')

print(td.strftime('%Y %m %d %H:%M:%S %f'))
print(td.year)
print(td.month)
print(td.day)

print('-----------------------------------')
#time 类表示由时、分、秒、微秒组成的时间

t = datetime.time(10, 10, 10)
print(t.isoformat())
print(t.replace(hour=9, minute=9))
print(t.strftime('%I:%M:%S %p'))
print(t.hour,t.minute,t.second,t.microsecond,t.tzinfo,)

print('-----------------------------------')
#datetime 包括了 date 与 time 的所有信息，
# 格式为：datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())                   	#根据时间戳返回对应UTC时间
print(datetime.datetime.fromtimestamp(time.time()))
print(datetime.datetime.utcfromtimestamp(time.time()))
print(datetime.datetime.combine(datetime.date(2019, 12, 1), datetime.time(10, 10, 10)))
print(datetime.datetime.min,datetime.datetime.max)

print('-----------------------------------')

td = datetime.datetime.today()
print(td.date())
print(td.time())
print(td.replace(day=11, second=10))
print(td.weekday())
print(td.isoweekday())

print('-----------------------------------')

print(td.isocalendar())
print(td.isoformat())
print(td.strftime('%Y-%m-%d %H:%M:%S.%f'))
print(td.year,td.month,td.hour,td.minute,td.second,td.microsecond,td.tzinfo,)

print('-----------------------------------')
#calendar 模块提供了很多可以处理日历的函数

calendar.setfirstweekday(1)
print(calendar.firstweekday())
print(calendar.isleap(2019))                 #如果 year 是闰年则返回 True ,否则返回 False
print(calendar.leapdays(1945, 2019))         #返回 y1 至 y2 （包含 y1 和 y2 ）之间的闰年的数量
print(calendar.weekday(2019, 12, 1))
print(calendar.monthrange(2019, 12))         #返回指定年份的指定月份第一天是星期几和这个月的天数
print('-----------------------------------')
print(calendar.month(2019, 12))
print('-----------------------------------------------------------------------------')
print(calendar.prcal(2019))


print('-----------------------------------')
#Calendar 对象提供了一些日历数据格式化的方法
#iterweekdays()  返回一个迭代器，迭代器的内容为一星期的数字
#itermonthdates(year, month)  返回一个迭代器，迭代器的内容为年 、月的日期


c = calendar.Calendar()
print(list(c.iterweekdays()))

for i in c.itermonthdates(2019, 12):
    print(i)
print('-----------------------------------')

#TextCalendar 为 Calendar子类，用来生成纯文本日历


from calendar import TextCalendar
tc = TextCalendar()
print(tc.formatmonth(2019, 12))
print(tc.formatyear(2019))

#HTMLCalendar 类可以生成 HTML 日历
from calendar import HTMLCalendar
hc = HTMLCalendar()
print(hc.formatmonth(2019, 12))
print(hc.formatyear(2019))
print(hc.formatyearpage(2019))
