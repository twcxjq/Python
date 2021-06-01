# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     py_iter
# Author:      TianChangJun
# Datetime:    2021/6/1 22:51
# Description：
# -----------------------------------

"""
迭代器的优势是内存开销更小，它比一次性加载数据占用的内存更小，适用于大数据量的计算。
"""
# print(sum(list(range(1,1000000001))))
# print(sum(iter(range(1,1000000001))))


list2 = [2, 4, 6, 8]
tuple1 = (3, 5, 7)
print(type(list2))
# 把列表变成迭代器
obj = iter(list2)
print(type(obj))
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
# print(obj.__next__())  # StopIteration

# print(next(obj))
# print(next(obj))

from collections.abc import Iterator

print(isinstance(list2, Iterator))  # 判断是否为迭代器
print(isinstance(obj, Iterator))    # 判断是否为迭代器

