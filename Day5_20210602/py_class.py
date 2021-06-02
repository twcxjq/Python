# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     py_class
# Author:      TianChangJun
# Datetime:    2021/6/2 14:53
# Description：类名一般首字母大写, 采用驼峰式命名,大驼峰: PythonClass  ,小驼峰: pythonClass
# -----------------------------------------------------------------------------------

# 定义类用class关键字, 定义方法def

class Person:
    height = 170
    weight = 90
    def __init__(self):
        print("这个是构造方法")
    def __del__(self):
        print("这个是析构方法")
    def speak(self, like):
        self.age = 18
        print("老王喜欢说唱，他今年{}岁了，他身高{},喜欢{}".format(self.age, self.height, like))

    def __str__(self):
        return "这个是对象说明方法"
    def run(self):
        shudu = 70
        print("跑的飞快,速度{}迈,她今年{}岁了".format(shudu, self.age))
        self.speak("add")

# 实例化对象,类名后面一定要加()
# 实例化出来的对象拥有这个类中所有的变量和方法
xiaohua = Person()
print(xiaohua)
# print(Person())
xiaohua.speak("篮球")
print(xiaohua.weight)
xiaohua.run()



