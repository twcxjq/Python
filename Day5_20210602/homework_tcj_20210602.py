# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     homework_tcj_20210602
# Author:      TianChangJun
# Datetime:    2021/6/2 15:08
# Description：
# -----------------------------------------------------------------------------------

"""
1、求列表里面所有数字(int)的和
list1 = [1,9,[2,8,[3,7]],(4,6),{1,9},{"姓名":"张三","年龄":10,2:8},"nihao"]
"""
# def list_int_sum(list1):
#     sum_int = 0
#     for item in list1:
#         if type(item) == int:
#             sum_int += item
#             return sum_int
#
#
#
# list1 = [1,9,[2,8,[3,7]],(4,6),{1,9},{"姓名":"张三","年龄":10,2:8},"nihao"]




"""
2, 冒泡排序:
将list = [7, 4, 3, 67, 34, 1, 8]中的数据从小到大排序，最后输出结果为：[1, 3, 4, 7, 8, 34, 67]：
提示冒泡排序，比较大小交换位置，或者用空杯交换原理
"""







"""
3、求1-2+3-4+5-6+7-8+9 ... 99的值
"""
item = 1
def jiajian(number):
    global item
    if number == 99:
        return 99
    if item % 2 != 0:
        item += 1
        return number - jiajian(number + 1)
    if item % 2 == 0:
        item += 1
        return number + jiajian(number + 1)

print(jiajian(1))




