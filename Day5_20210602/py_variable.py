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





cucumber = "小黄瓜"  # 全局变量，函数外，写在调用之前，所有函数都能直接使用


def dog():
    food = "骨头"  # 局部变量, 函数内，只能在函数内部使用
    print("旺财喜欢{},还喜欢吃{}".format(food, cucumber))


def cat():
    like = "骨头"  # 局部变量, 函数内，只能在函数内部使用
    global cucumber  # 声明要修改的全局变量
    cucumber = "大黄瓜"
    print("tom喜欢{},还喜欢吃{}".format(like, cucumber))

cat()
dog()
print(cucumber)
