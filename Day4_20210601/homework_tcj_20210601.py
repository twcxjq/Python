# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     homework_tcj_20210601
# Author:      TianChangJun
# Datetime:    2021/6/1 12:50
# Description：
# -----------------------------------------------------------------------------------

import random

"""
猜字小游戏
总共5次机会，每猜错一次，机会减一，
当机会用完，提示是否继续！
如果继续就重新给5次机会，如果不继续就跳出程序
判断用户输入的是否为0-100的整数，如果不是则重新输入
"""
# number = random.randint(1, 100)   #闭区间(左右都可以取到)
# choice_number = 5
#
# while True:
#     if choice_number > 0:
#         user_number = input("请输入一个1-100范围内的整数: ")
#     user_number_int = int(user_number)
#     if user_number.isdigit() and user_number_int >= 1 and user_number_int <= 100:
#         if user_number_int == number:
#             print("恭喜你,猜对了!!!")
#             break
#         elif user_number_int > number:
#             if choice_number > 0:
#                 choice_number -= 1
#                 print("你猜的数字大了，请重新猜, " + "你还剩下{}次机会".format(choice_number))
#             elif choice_number == 0:
#                 user_chice = input("五次机会以用完, 是否继续游戏, 如果继续请输入y,如果不继续请输入n: ")
#                 if user_chice == "y":
#                     choice_number = 5
#                 elif user_chice == "n":
#                     print("游戏结束, 欢迎下次来玩啊!!!")
#                     break
#         else:
#             if choice_number > 0:
#                 choice_number -= 1
#                 print("你猜的数字小了，请重新猜, " + "你还剩下{}次机会".format(choice_number))
#             elif choice_number == 0:
#                 user_chice = input("五次机会以用完, 是否继续游戏, 如果继续请输入y,如果不继续请输入n: ")
#                 if user_chice == "y":
#                     choice_number = 5
#                 elif user_chice == "n":
#                     print("游戏结束, 欢迎下次来玩啊!!!")
#                     break
#     else:
#         print("输入数字有误!!!")




"""
2, 打印如下图形
"""
# total = 4
# for i in range(1, total + 1):
#     if i == 2:
#         print(" " * (total - i) + "*" + " " * (i * 2 - 3) + "*")
#     elif i == 3:
#         print(" " * (total - i) + "*" + " " * (i * 2 - 3) + "*")
#     else:
#         print(" " * (total - i) + "*" * (i * 2 - 1))

"""
3、dict1 = {"小花":18,"小兰":20,10:20}，
判断dict1的是不是字典，如果是字典，把字典里的偶数进行相加，最后输出和
"""
# dict1 = {"小花":18,"小兰":20,10:20}
# if (isinstance(dict1, dict)):
#     list_kv = []
#     for k in dict1.keys():
#         if type(k) == int and k % 2 == 0:
#             list_kv.append(k)
#     for v in dict1.values():
#         if type(v).__name__ == "int" and v % 2 == 0:
#             list_kv.append(v)
#     print("字典里的偶数和为{}".format(sum(list_kv)))
# else:
#     print("不是字典")


"""
4、使用while循环输出 1 2 3 4 5 6 8 9 10
"""
# item = 1
# while item <= 10:
#     if item != 7:
#         print(item)
#     item += 1


"""
5、打印水仙花数
    水仙花数是指一个 n 位数（n≥3 ），它的每个位上的数字的 n 次幂之和等于它本身
    例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。153 = 1**3+5**3+3**3
    利用for循环输出1000以内的水仙花数
"""
# list_item_str = []
# num = 0
# for item in range(100, 1000):
#     item_str = str(item)
#     list_item_str.append(item_str)
# # print(list_item_str)
# # print(list_item_str[0][0])
# for list_vlaue in  list_item_str:
#     if int(list_vlaue[0]) ** 3 + int(list_vlaue[1]) ** 3 + int(list_vlaue[2]) ** 3 == int(list_vlaue):
#         item_str = int(list_vlaue)
#         print(item_str)
#         num += 1
# print("1000以内的水仙花数共有{}个".format(num))


"""
6、打印九九乘法表（方法不限）
"""
for num1 in range(1, 10):
    for num2 in range(1, num1 + 1):
        print("{}X{}={}".format(num2, num1, num1 * num2), end="\t")
    print()







