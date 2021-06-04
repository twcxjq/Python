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
    _height = 170   # 公用成员变量私有化   用_或者__
    __weight = 90  # 外部调用的时候，名字会被重命名: _类名__变量名
    def __init__(self, shuoming):
        print("这个是构造方法{}".format(shuoming))
    def __del__(self):
        print("这个是析构方法")
    def _speak(self, like):    # 公用成员方法私有化   用_或者__
        self.age = 18        # 私有变量公有化，用self，别的方法就可以调用这个变量了
        print("老王喜欢说唱，他今年{}岁了，他身高{},他体重{},喜欢{}".format(self.age, self._height, self.__weight, like))

    def __str__(self):
        return "这个是对象说明方法"
    def __run(self):
        shudu = 70      # 方法内部的变量叫(这个方法的)私有变量，属于这个方法私有,别的方法无法调用这个私有变量
        print("跑的飞快,速度{}迈,她今年{}岁了".format(shudu, self.age))  # 同一个类中,调用公有变量age，使用self
        self._speak("add")

# 实例化对象,类名后面一定要加()
# 实例化出来的对象拥有这个类中所有的变量和方法
xiaohua = Person("说明")
print(xiaohua)
# print(Person())
xiaohua._speak("篮球")
print(xiaohua._Person__weight, xiaohua._height)
xiaohua._Person__run()



