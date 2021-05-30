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

# 如何将前10个整数的平方加入到一个列表中
squares = []
for item in range(1, 11):
    squares.append(item ** 2)
print(squares)
print(min(squares))
print(max(squares))
print(len(squares))
print(sum(squares))




