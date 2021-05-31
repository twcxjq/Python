# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     py_dict
# Author:      TianChangJun
# Datetime:    2021/5/31 14:35
# Description：
# -----------------------------------------------------------------------------------

# 创建一个空字典
dict1 = {}
print(type(dict1), len(dict1))

# 创建一个非空字典
dict2 = {"姓名": "老王", "年龄": 22, "来自": "成都", "喜欢": ["小花", "小兰", "刘三"], 55: 66}
print(type(dict2), len(dict2))

'''
# 取值
# 打印老王， 通过K获取对应的V值
print(dict2["姓名"])  # 如果不存在报KeyError
print(dict2.get("姓名"))  # 如果不存在不报错, 返回None

# 把22修改成99
print("修改前:", dict2)
dict2["年龄"] = 99
print("修改后:", dict2)
# 把小兰改成小张
print("修改前:", dict2)
dict2["喜欢"][1] = "小张"
print("修改后:", dict2)

# 新增一个键值对
print("新增前:", dict2)
dict2["小龙女"] = 999
print("新增后:", dict2)
# 新增多个键值对
print("新增前:", dict2)
dict3 = {1: 3, 2: 4}
dict_d = {"头发": "绿色"}
dict2.update(dict3)
print("新增后:", dict2)
'''

"""
print("删除前:", dict2)
print(dict2.pop("喜欢"))  # 如果K不存在，则报KeyError
print("删除后:", dict2)

print("删除前:", dict2)
print(dict2.popitem())  # 默认删除最后一个键值对
print("删除后:", dict2)

print("删除前:", dict2)
del dict2["年龄"]
print("删除后:", dict2)
"""

# print(len(dict2))
# print(dict2.copy())
# dict2.clear()
# print(dict2)

dict3 = {"姓名": "老王", "年龄": 22, "来自": "成都", "喜欢": ["小花", "小兰", "刘三"], 55: 66}
for k in dict3.keys():
    print(k)
print(dict3.keys())  # dict_keys(['姓名', '年龄', '来自', '喜欢', 55])
print(list(dict3.keys()))  # ['姓名', '年龄', '来自', '喜欢', 55]
for v in dict3.values():
    print(v)
print(dict3.values())  # dict_values(['老王', 22, '成都', ['小花', '小兰', '刘三'], 66])
print(list(dict3.values()))  # ['老王', 22, '成都', ['小花', '小兰', '刘三'], 66]
for k, v in dict3.items():
    print(k, ":", v)


"""
从键盘输入一个年份，判断它是闰年还是平年？
闰年：普通年能被四整除且不能被100整除的为闰年，能被400整除的也是闰年
"""
# year = int(input("请输入一个年份: "))
# print("闰年" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else "平年")

# 打印每一个键值对中键所对应的值
for k in dict3.keys():
    print(dict3[k])

# 打印每一个键值对中键所对应的值
for v in dict3.values():
    print(v)

# 打印每一个键值对中键（不推荐）
for item in dict3:
    print(item)

# 打印每一个键值对中键
for k in dict3.keys():
    print(k)













