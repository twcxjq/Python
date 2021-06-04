# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     py_time
# Author:      TianChangJun
# Datetime:    2021/6/4 15:43
# Description：
# -----------------------------------------------------------------------------------

import time
import datetime

print(time.time())
# 结构时间
print(time.gmtime())
print(time.gmtime(time.time()))
print(time.localtime())
print(time.localtime(time.time()))
# 英文时间
print(time.asctime())
print(time.asctime(time.localtime(time.time())))
print(time.asctime(time.gmtime(time.time())))
# 自定义时间
print(time.strftime("%Y/%m/%d:%H-%M-%S"))


# 打印当前时间
print(datetime.datetime.now())
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)
print(datetime.datetime.now().hour)
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)
print(datetime.datetime.now().weekday())
print(datetime.datetime.now().microsecond)

# 查看日期对应是星期几
print(datetime.date(2021, 6, 4).weekday())
print(datetime.date(1997, 8, 5).weekday())
