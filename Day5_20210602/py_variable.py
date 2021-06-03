# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     py_variable
# Author:      TianChangJun
# Datetime:    2021/6/2 13:03
# Description：
# -----------------------------------------------------------------------------------

# cucumber = "小黄瓜"  # 全局变量，函数外，写在调用之前，所有函数都能直接使用
#
#
# def dog():
#     food = "骨头"  # 局部变量, 函数内，只能在函数内部使用
#     print("旺财喜欢{},还喜欢吃{}".format(food, cucumber))
#
#
# def cat():
#     like = "骨头"  # 局部变量, 函数内，只能在函数内部使用
#     print("tom喜欢{},还喜欢吃{}".format(like, cucumber))
#
#
# dog()
# cat()





# cucumber = "小黄瓜"  # 全局变量，函数外，写在调用之前，所有函数都能直接使用
#
#
# def dog():
#     food = "骨头"  # 局部变量, 函数内，只能在函数内部使用
#     print("旺财喜欢{},还喜欢吃{}".format(food, cucumber))
#
#
# def cat():
#     like = "骨头"  # 局部变量, 函数内，只能在函数内部使用
#     global cucumber  # 声明要修改的全局变量
#     cucumber = "大黄瓜"
#     print("tom喜欢{},还喜欢吃{}".format(like, cucumber))
#
# cat()
# dog()
# print(cucumber)


# # 正常逻辑求1-100的和
#
# def add(number):
#     he = 0
#     num = 1
#     while num <= number:
#         he += num
#         num +=1
#     return he
#
# print(add(100))

# # 函数递归的方法求1-100的和
# def he(number):
#     if number == 1:
#         return 1
#     return number + he(number - 1)
#
# print(he(100))

# # 函数递归的方法求1-100的和
# def he(number):
#     if number == 100:
#         return 100
#     return number + he(number + 1)
#
# print(he(1))

# # 函数递归的方法求1*2*3*4*5的积
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
# print(fact(5))

# # 函数递归的方法求1*2*3*4*5的积
# def fact(n):
#     if n == 5:
#         return 5
#     return n * fact(n + 1)
# print(fact(1))

