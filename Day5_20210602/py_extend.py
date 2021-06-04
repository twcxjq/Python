# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     py_extend
# Author:      TianChangJun
# Datetime:    2021/6/3 16:34
# Description：
# -----------------------------------------------------------------------------------

"""
class Pig:
    name = "八戒"
    def jiao(self):
        print("猪叫")

class Dog:
    def eat(self):
        print("狗吃东西")
    def jiao(self):
        print("狗叫")

class Cat:
    def zhualaoshu(self):
        print("猫抓老鼠")

class Monkey(Pig, Dog, Cat):
    def chitao(self):
        print("猴吃桃子")


wukong = Monkey()
# wukong.chitao()
# print(wukong.name)
# wukong.zhualaoshu()
# wukong.eat()
wukong.jiao()   # 调用多继承方法，方法名同，默认调用的是在括号中排前的父类的方法
"""


"""
class Cat:
    def jiao(self):
        print("猫叫")
    def zhualaoshu(self):
        print("猫抓老鼠")

class Monkey(Cat):
    def chitao(self):
        print("猴吃桃子")
    # 调用与重写父类方法前提条件：1、必须继承父类，2、方法名和父类的方法名一致   
    def jiao(self):
        print("猴叫")


wukong = Monkey()
wukong.jiao()   # 猴叫
"""



"""
# 父类的一个方法被不同的子类重写,实现了不同的行为,这个方法表现出来的就是多态行为

class Pig:
    name = "八戒"
    def jiao(self):
        print("猪叫")

class Dog(Pig):
    def eat(self):
        print("狗吃东西")
    def jiao(self):
        print("狗叫")

class Cat(Pig):
    def zhualaoshu(self):
        print("猫抓老鼠")
    def jiao(self):
        print("猫叫")

class Monkey(Pig):
    def chitao(self):
        print("猴吃桃子")
    def jiao(self):
        print("猴叫")


d = Dog()
d.jiao()
c = Cat()
c.jiao()
m = Monkey()
m.jiao()
"""



"""
class Cat:
    def jiao(self):
        print("猫叫")
    def zhualaoshu(self):
        print("猫抓老鼠")

class Monkey(Cat):
    def chitao(self):
        print("猴吃桃子")
    # 重写父类jiao()方法
    def jiao(self):
        print("猴叫")
    def super_jiao(self):
        super().jiao()
        super(Monkey, self).jiao()


wukong = Monkey()
wukong.jiao()
wukong.super_jiao()
"""



class Cat:
    def jiao(self):
        print("猫叫")
    def zhualaoshu(self):
        print("猫抓老鼠")
    @staticmethod  # 装饰器，作用是在不改变被装饰函数的前提条件下，增加被装饰函数的功能
    def jintai():
        print("这是静态方法")


tom = Cat()
tom.jintai()
# 静态方法可以直接使用类名.方法名调用，作用域只对下方的第一个方法有用
Cat.jintai()



