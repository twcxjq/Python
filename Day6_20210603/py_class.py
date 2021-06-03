# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     py_class
# Author:      TianChangJun
# Datetime:    2021/6/3 11:37
# Description：
# -----------------------------------------------------------------------------------

# class Person():
#     name = "大黄"
#
# class child1(Person):
#     pass
# class child2(Person):
#     pass
#
# print(Person.name, child1.name, child2.name)  # 大黄 大黄 大黄
# child1.name = "小黄"
# print(Person.name, child1.name, child2.name)  #  大黄 小黄 大黄
# Person.name = "花花"
# print(Person.name, child1.name, child2.name)  # 花花 小黄 花花


class Person:
    def __init__(self):
        print("这是父类的构造方法")

class Dog(Person):
    def __init__(self):
        print("这是子类的构造方法")
        super().__init__()
        # Person().__init__()
    def eat(self):
        print("狗吃骨头")

if __name__ == '__main__':
    dog = Dog()
    dog.eat()


