# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     py_tuple
# Author:      TianChangJun
# Datetime:    2021/5/31 10:34
# Description：
# -----------------------------------------------------------------------------------

# 创建一个空元组(tuple)
tuple1 = ()
print(type(tuple1), len(tuple1))

# 创建一个非空元组
tuple2 = ("h",)  # 只有一个元素的时候, 需要在元素后面加上 ,
print(type(tuple2), len(tuple2))
print(tuple2)

# 类型转换
num = 22
name = "你好"
list1 = [33, 22]
tuple3 = (66, 99)

aa = str(num)
print(type(aa), aa)
bb = tuple(list1)
print(type(bb), bb)
cc = list(tuple3)
print(type(cc), cc)

tuple4 = (1, 4, 5, 6)
tuple5 = ("你好", "吗")
print(tuple4 + tuple5)
print(tuple4, tuple5)
print(tuple4 * 3)

a = tuple4[::-1]
print(a)
print(id(tuple4))
print(id(a))    # 被修改后的对象是另存的内存地址，原对象没有被修改

tuple5 = (2, 4, 6, 8)
tuple_list = list(tuple5)
tuple_list[-1] = 99
tuple5 = tuple(tuple_list)
print(tuple5)

"""
1、把元组(2,4,6,8)改成(2,4,6,99)
2、统计元组（33,3,4,6,8,3,99,55）中3的次数并打印出它的索引位置
"""
tuple6 = (33, 3, 4, 6, 8, 3, 99, 55)
count = tuple6.count(3)
print(count)
index = -1
for item in tuple6:
    index += 1
    if item == 3:
        print(index, item)

# print(tuple6.index(3))  # 找到第一个目标元素的索引位置并返回








