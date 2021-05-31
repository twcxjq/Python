# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     py_tz
# Author:      TianChangJun
# Datetime:    2021/5/30 23:28
# Description：
# -----------------------------------

# list1 = [44, 7]
# s = str(list)
# print((type(s)))
# print(s)


# for value in range(1, 5):
#     print(value)
# print(type(range(1, 5)))
# number = list(range(1, 5))
# print(number)

# # 使用函数range() 时，还可指定步长。例如，下面的代码打印1~10内的偶数
# even_number = list(range(2, 11, 2))
# print(even_number);
# for item in even_number:
#     print(item)

"""
# 如何将前10个整数的平方加入到一个列表中
squares = []
for item in range(1, 11):
    squares.append(item ** 2)
print(squares)
print(min(squares))
print(max(squares))
print(len(squares))
print(sum(squares))
"""

"""
# 1, 使用一个for 循环打印数字1~20（含）
for item in range(1, 21):
    print(item)
"""


"""
2,  ：创建一个列表，其中包含数字1~1 000 000，
再使用一个for 循环将这些数字打印出来（如果输出的时间太长，按Ctrl+ C停止输出，或关闭输出窗口）
"""
list_number = []
for item in range(1, 101):
    list_number.append(item)
print(list_number)


"""
3, 创建一个列表，其中包含数字1~1 000 000，再使用min() 和max() 核实该列表确实是从1开始，到1 000 000结束的。
另外，对这个列表调用函数sum() ，看看Python将一百万个数字相加需要多长时间。
"""
list_number1 = []
for item in range(1, 101):
    list_number1.append(item)
print(list_number1)
print(min(list_number1))
print(max(list_number1))
print(sum(list_number1))

"""
 4, 通过给函数range() 指定第三个参数来创建一个列表，其中包含1~20的奇数；
 再使用一个for 循环将这些数字都打印出来。
"""
list_number2 = []
for item in range(1, 21, 2):
    list_number2.append(item)
for item in list_number2:
    print(item)

"""
 5, 创建一个列表，其中包含3~30内能被3整除的数字；再使用一个for 循环将这个列表中的数字都打印出来
"""
# 创建一个空列表
list_number3 = []
for item in range(3, 31):
    if item % 3 == 0:
        list_number3.append(item)
for item in list_number3:
    print(item)


