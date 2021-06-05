# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     py_pratise
# Author:      TianChangJun
# Datetime:    2021/6/5 15:18
# Description：
# -----------------------------------------------------------------------------------

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# dimensions[0] = 100
print(dimensions[0])
for item in dimensions:
    print(item)

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

