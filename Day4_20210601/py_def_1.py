# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     py_def_1
# Author:      TianChangJun
# Datetime:    2021/6/1 23:07
# Description：
# -----------------------------------

# # 使用def定义person函数
# # def person(name, age):  # 定义函数的时候,括号的叫形参
# #
# #     print("老王喜欢{}, 今年{}岁了".format(name, age))
# #
# #
# # # 调用函数
# # person("兰兰", 18)  # 调用实际传入的参数叫实参


# # 使用def定义person函数
# def person(name, age):  # 定义函数的时候,括号的叫形参(这里的name和age称为位置参数(必须参数))
#
#     print("老王喜欢{}, 今年{}岁了".format(name, age))
#
#
# # 调用函数
# person("兰兰", 18)  # 调用实际传入的参数叫实参


# # 使用def定义person函数
# # 定义函数的时候,括号的叫形参(这里的name和age称为位置参数(必须参数))
# # 默认参数（缺省参数）：默认参数要靠右--这里age是默认参数.但age处于color前面时,color显示non-default...
# def person(name, color, age=18):
#     print("老王喜欢{}, 今年{}岁了, 头发颜色是{}".format(name, age, color))
#
#
# # 调用函数
# # 调用实际传入的参数叫实参
# # 调用函数的时候默认参数不传值，使用默认的值
# # person("兰兰", "绿色")
# #调用函数的时候默然参数传值，使用新传入的值
# person("兰兰", "绿色", 99)


# 使用def定义person函数
# 定义函数的时候,括号的叫形参(这里的name和age称为位置参数(必须参数))
# 默认参数（缺省参数）：默认参数要靠右--这里age是默认参数.但age处于color前面时,color显示non-default...
def person(name, color="green", age=18):
    print("老王喜欢{}, 今年{}岁了, 头发颜色是{}".format(name, age, color))


# 调用函数
# 调用实际传入的参数叫实参
# 调用函数的时候默认参数不传值，使用默认的值
# person("兰兰", "绿色")
# 调用函数的时候默然参数传值，使用新传入的值
person("兰兰", age=99, color="绿色")  # 这里的age和name称为关键字参数


def dog(a, b, *c):
    print(a)
    print(b)
    print(c)


dog(1, 2, 3, 4, 5, 6)


def dog(a, b, **c):
    print(a)
    print(b)
    print(c)


dog(1, 2, age=3, weight=180)


def pig(a, b, *c, **d):
    print(a)
    print(b)
    print(c)
    print(d)


pig(1, 2, 3, 4, 5, age=3, weight=180)


def monkey(a, b, c, *d):
    print(a)
    print(b)
    print(c)
    print(d)


monkey(*(1, 2, 3, 4, 8, 9, 0))
monkey(11, 22, 33, *(1, 2, 3, 4, 8, 9, 0))




def monkey(a, b, c, *d, **e):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

data = (1, 2, 3, 4, 8, 9, 0)
monkey(*data)

dict1 = {"小花": 18, "喜欢": "老王"}
monkey(1, 2, 3, 4, 4, 7, 8, 9, **dict1)
monkey(1, 2, 3, 4, name="老王", age=10)



def monkey(a, b, c, f = 33, *d, **e):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)

data = (1, 2, 3, 4, 8, 9, 0)
monkey(*data)

dict1 = {"小花": 18, "喜欢": "老王"}
monkey(1, 2, 3, 44, 4, 7, 8, 9, **dict1)
monkey(1, 2, 3, 4, name="老王", age=10)


def cat():
    xiezi = "高跟鞋"
    waiyi = "风衣"
    return xiezi  # 返回值后就结束代码运行
    return waiyi

print(cat())

def cat1():
    xiezi = "高跟鞋"
    waiyi = "风衣"
    return xiezi, waiyi

print(cat1())

def num(a=4, b=1):
    if a > 2:
        print(a)
        return a
    if b > 1:
        print(b)
        return b

print(num())
