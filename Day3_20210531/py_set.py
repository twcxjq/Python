# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     py_set
# Author:      TianChangJun
# Datetime:    2021/5/31 16:35
# Description：
# -----------------------------------------------------------------------------------

# 创建空集合
set1 = set()
print(type(set1), len(set1))
print(set1)

# 创建非空集合
set2 = {1, 3, 5, 7, 9}
print(type(set2), len(set2))
print(set2)

set3 = set((2, 4, 6))  # 传一个可迭代的对象
print(type(set3), len(set3))
print(set3)

set3_1 = set("hh")  # 传一个可迭代的对象
print(type(set3_1), len(set3_1))    # <class 'set'> 1
print(set3_1)

set3_2 = set("ho")  # 传一个可迭代的对象
print(type(set3_2), len(set3_2))    # <class 'set'> 2
print(set3_2)

set4 = {1, 2, 3, 4, 5}
set5 = {4, 5, 6, 7, 8}
# 交集 取两个集合相同的元素构成一个新的集合
print(set4 & set5)
print(set4.intersection(set5))

# 并集 取两个集合的所有元素构成一个新的集合并去除相同的元素
print(set4 | set5)
print(set4.union(set5))

# 差集 取集合中唯一的组成一个新的集合
print(set4 - set5)
print(set4.difference(set5))

print(set5 - set4)
print(set5.difference(set4))

# 对称差集  取两个集合的交集，然后根据交集取两个集合的补集，最后将补集取并集
print(set4 ^ set5)
print(set4.symmetric_difference(set5))

set6 = {1, 3, 4, 7, 5}
print("新增前:", set6)
set6.add((77, 6))   # 不可变元素
set6.add("ab")
print("新增后:", set6)

print("新增前:", set6)
set6.update([77, 66])
print("新增后:", set6)

set7 = {1, 2, 3, 44, 55, 66}
print("删除前:", set7)
set7.pop()
print("删除后:", set7)

set8 = {"淘宝", "京东", "拼多多", "唯品会"}
print("删除前:", set8)
print(set8.pop())
print("删除后:", set8)

print("删除前:", set8)
del set8
# print("删除后:", set8)
