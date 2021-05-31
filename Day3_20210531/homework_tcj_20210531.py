# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     homework_tcj_20210531
# Author:      TianChangJun
# Datetime:    2021/5/31 17:50
# Description：
# -----------------------------------------------------------------------------------

"""
1、元组tuple2 = (3,4,5,11,1,88)
    1）、求最大值
    2）、求最小值
    3）、把tuple2转换成列表和字符串类型
    4）、把3)题中转换后得到的列表中的88，改成{"喜欢":"打球"}
"""
# 创建一个非空元组tuple2
tuple2 = (3, 4, 5, 11, 1, 88)
# 求最大值
print(max(tuple2))
# 求最小值
print(min(tuple2))
# 把tuple2转换成列表和字符串类型
tuple_list = list(tuple2)
print(type(tuple_list))
tuple_str = str(tuple2)
print(type(tuple_str))
# 把3)题中转换后得到的列表中的88，改成{"喜欢":"打球"}
print("修改前:", tuple_list)
tuple_list[-1] = {"喜欢": "打球"}
print("修改后:", tuple_list)

"""
2、dict3 = {"名人":["诗人","李白"],"天气":"晴朗"}
    1）、添加一个新的键值对："城市":"成都"
    2）、把李白，改成杜甫
    3）、把{"阿朱":16,"阿紫":15,"周芷若":18}添加到dict3中
    4）、最后打印所有的K和V
"""
dict3 = {"名人": ["诗人", "李白"], "天气": "晴朗"}
# 添加一个新的键值对："城市":"成都"
# print("新增前:", dict3)
# dict3["城市"] = "成都"
# print("新增后:", dict3)

# 添加一个新的键值对："城市":"成都"
print("新增前:", dict3)
dict3_increment = {"城市": "成都"}
dict3.update(dict3_increment)
print("新增后:", dict3)

# 把李白，改成杜甫
print("修改前: ", dict3)
dict3["名人"][1] = "杜甫"
print("修改后: ", dict3)

# 把{"阿朱":16,"阿紫":15,"周芷若":18}添加到dict3中
print("新增前:", dict3)
dict3_increment1 = {"阿朱": 16, "阿紫": 15, "周芷若": 18}
dict3.update(dict3_increment1)
print("新增后:", dict3)

# 最后打印所有的K和V
for k, v in dict3.items():
    print(k, ":", v)

"""
3, 使用if，编写程序，实现以下功能：
    从键盘获取用户名、密码
    如果用户名和密码都正确（预先设定一个用户名和码），
    那么就显示“欢迎进入完美世界”，否则提示密码或者用户名错误
"""
# username_input = input("请输入用户名:")
# password_input = int(input("请输入密码:"))
# username_true = "zxy"
# password_true = 216
# if username_input == username_true and password_input == password_true:
#     print("欢迎进入完美世界")
# else:
#     print("密码或者用户名错误")

"""
4, 从键盘输入一个整数，判断这个整数是正数还是负数，如果是正数再判断是偶数还是奇数
"""
# number = int(input("请输入一个整数:"))
# if number > 0:
#     print("这个整数是正数")
#     if number % 2 == 0:
#         print("这个整数是正数并且是偶数")
#     else:
#         print("这个整数是正数并且是奇数")
# elif number == 0:
#     print("这个整数是0")
# else:
#     print("这个整数是负数")

"""
5, 从键盘输入一个整数，如果这个数能被3整除且不能被5整除就输出该整数，否则就输出不符合规则
"""
# number1 = int(input("请输入一个整数:"))
# if number1 % 3 == 0 and number1 % 5 != 0:
#     print("输入的整数是:", number1)
# else:
#     print("输入的整数不符合规则")

"""
6, 有1、2、3、4个数字，能组成哪些互不相同且不重复的三位数？
"""
str1, str2, str3, str4 = str(1), str(2), str(3), str(4)
# print(type(str1), str1)
list_str_number = []
list_str_number.append(str1)
list_str_number.append(str2)
list_str_number.append(str3)
list_str_number.append(str4)
# 创建一个空集合
set_number = set()

for item1 in list_str_number:
    for item2 in list_str_number:
        for item3 in list_str_number:
            if item1 != item2 and item2 != item3 and item3 != item1:
                str_combination = item1 + item2 + item3
                number_combination = int(str_combination)
                set_number.add(number_combination)
print(set_number)
print("能够组合互不相同且不重合的三位数个数为: {}".format(len(set_number)))
