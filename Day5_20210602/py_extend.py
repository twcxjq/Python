# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     py_extend
# Author:      TianChangJun
# Datetime:    2021/6/3 16:34
# Description：
# -----------------------------------------------------------------------------------

class Pig:
    name = "八戒"
    def jiao(self):
        print("猪叫")

class Dog:
    def eat(self):
        print("狗吃东西")

class Cat:
    def zhualaoshu(self):
        print("猫抓老鼠")

class Monkey(Pig, Dog, Cat):
    def chitao(self):
        print("猴吃桃子")


wukong = Monkey()
wukong.chitao()
print(wukong.name)
wukong.zhualaoshu()
wukong.eat()
