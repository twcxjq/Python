# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     number_writer
# Author:      TianChangJun
# Datetime:    2021/6/5 17:16
# Description：
# -----------------------------------------------------------------------------------

"""
模块json 让你能够将简单的Python数据结构转储到文件中，并在程序再次运行时加载该文件中的数据
"""

"""
我们来编写一个存储一组数字的简短程序，再编写一个将这些数字读取到内存中的程序。
第一个程序将使用json.dump() 来存储这组数字，而第二个程序将使用json.load() 。
"""

import json

numbers = [2, 3, 5, 7, 11, 13]
filename = "numbers.json"
with open(filename, mode="w") as f_obj:
    json.dump(numbers, f_obj)












