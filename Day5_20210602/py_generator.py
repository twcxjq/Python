# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     py_generator
# Author:      TianChangJun
# Datetime:    2021/6/2 11:44
# Description：
# -----------------------------------------------------------------------------------


# def generator():
#     yield 1     # 使用yield关键字把函数变成生成器(生成器的本质就是一个迭代器)
#     yield 2
#     yield 3
#     yield 4
#
# # 函数运行时遇到yield后先返回再挂起，再次使用函数名多次调用，四次调用都会打印1
# print(generator().__next__())
# print(generator().__next__())
# print(generator().__next__())
# print(generator().__next__())
# print(next(generator()))


def generator():
    yield 1     # 使用yield关键字把函数变成生成器(生成器的本质就是一个迭代器)
    yield 2
    yield 3
    yield 4

# 函数运行时遇到yield后先返回再挂起，再次使用函数名多次调用，四次调用都会打印1
# print(generator().__next__())
# print(generator().__next__())
# print(generator().__next__())
# print(generator().__next__())
# print(next(generator()))

# 定义一个变量指向genetator对象的引用(相当于一个指针),
# 每一次调用gt都会开辟一个新的内存空间,四次分别打印1,2,3,4
gt = generator()
print(gt.__next__())
print(gt.__next__())
print(gt.__next__())
print(next(gt))

print(type((i for i in range(11))))
# 创建一个生成器
print((i for i in range(11)))

