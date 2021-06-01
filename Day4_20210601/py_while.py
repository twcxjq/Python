# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     py_while
# Author:      TianChangJun
# Datetime:    2021/6/1 11:00
# Description：
# -----------------------------------------------------------------------------------

# 求1—100的和
# item, sum_num = 1, 0
# while item <= 100:
#     sum_num += item
#     item += 1
# else:
#     print(sum_num)

# num = "*"
# for i in range(6):
#         print(num*i)

# num = "*"
# for i in range(1, 8, 2):
#         print(num*i)


# num, item = "*", 3
# for i in range(1, 8, 2):
#     print(" " * item + num * i)
#     item -= 1

# 求1-100所有偶数的和
# 列表推导式 [结果for 变量 in 可迭代对象] 或者 [结果 for 变量 in 可迭代对象 if 布尔表达式]


print([i for i in range(1, 101) if i % 2 == 0])

# 字典推导式 {结果for 变量 in 迭代对象} 或者 {结果 for 变量 in 迭代对象 if 布尔表达式}；
# 注意字典推导式的结果是键值对，即key:value
dict1 = {"小花": 19, "张三": 20, "身高": 180, "体重": 180}
print({k: v for k, v in dict1.items()})    # 键值对k:v
# 交换k与v
print({v: k for k, v in dict1.items()})  #{19: '小花', 20: '张三', 180: '体重'}   k不能重复

dict2 = {"小花": 19, "张三": 20, "身高": 180, "体重": "180"}
print({v: k for k, v in dict2.items()})   # {19: '小花', 20: '张三', 180: '身高', '180': '体重'}

# 集合推导式 {结果for 变量 in 迭代对象} 或者 {结果 for 变量 in 迭代对象 if 布尔表达式}
dict3 = {"小花": 19, "张三": 20, "身高": 180, "体重": 180}
print({k for k in dict3.keys()})
print({v for v in dict3.values()})   # 集合自动去重

print({v for v in dict2.values()})   # 集合自动去重


num = 10
name = "小花"
list1 = [2, 3, 4]
# 1)对象方法的调用有没有   __iter__()
name.__iter__()
list1.__iter__()

# 2)用dir()函数来查询是否包含__iter__()方法
print(dir(name))
if "__iter__" in dir(name):
    print("是可迭代对象")
else:
    print("不是可迭代对象")

# 3)通过内置的实例对象函数isinstance判断，
# 可迭代对象是Iterable类的实例，返回True就说明是可迭代对象，False则表示不是可迭代对象。
from collections.abc import Iterable

print(isinstance(num, Iterable))
print(isinstance(name, Iterable))

# print(sum(list(range(1,1000000001))))
print(sum(iter(range(1,1000000001))))


