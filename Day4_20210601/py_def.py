# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     py_def
# Author:      TianChangJun
# Datetime:    2021/6/1 16:07
# Description：
# -----------------------------------------------------------------------------------

# 定义函数
def person(name, color = "grean", age = 18):    # 默认参数要靠右
    print("老王喜欢{}, 今年{}岁了,头发颜色是{}".format(name, age, color))

# 调用函数
# person("兰兰", "红色")   # 使用默认参数age = 18
# person("兰兰", "红色", 99)   # 覆盖默认参数
# person("兰兰", age = "22", color="红色")    # 使用关键字参数时，允许函数调用时参数的顺序与声明时不一致
# person("小花")

