# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     py_read_csv
# Author:      TianChangJun
# Datetime:    2021/6/3 11:38
# Description：
# -----------------------------------------------------------------------------------

"""
读取csv文件数据第一中方法：列表的形式
"""
# import csv
# file1 = open(r"c:\test.csv", mode="r")  # 打开返回文件对象, 默认权限是读("r")
# data = csv.reader(file1)
# # print(data)
# for i in data:  # 数据存放在列表中的, 可以通过列表的下标索引进行取值
#     # print(i)
#     if i[0] != "姓名":
#         print("老王的女儿叫{},今年{}岁了".format(i[0], i[1]))
# file1.close()  # 关闭文件


"""
读取csv文件数据第二种方法：以字典的形式
"""
# import csv
# file1 = open(r"c:\test.csv", mode="r")
# data = csv.DictReader(file1)
# for i in data:  # 数据存放在字典中的, 可以通过键名进行取值
#         print("老王的女儿叫{},今年{}岁了".format(i["姓名"], i["年龄"]))
# file1.close()  # 关闭文件

"""
读取文件方法二：with open
"""
# import csv
# with open(r"c:\test.csv", mode="r") as f1:
#     data = csv.reader(f1)
#     for i in data:
#         if i[0] != "姓名":
#             print("老王的女儿叫{},今年{}岁了".format(i[0], i[1]))
#
#


"""
方法一：以列表的形式写入内容到csv文件：
"""
# import csv
# file2 = open(r"c:\test1.csv", mode="a", newline="")
# text = csv.writer(file2)
# text.writerow(["姓名", "年龄"])
# text.writerow(["大大", "12"])
# text.writerow(["小小", "13"])

"""
方法二：以字典的形式写入内容到csv文件：
"""
# import csv
# file2 = open(r"c:\test2.csv", mode="a", newline="")
# filedname = ["姓名", "年龄"]
# text = csv.DictWriter(file2, filedname)
# # 写表头
# text.writeheader()
# text.writerow({"姓名": "花花", "年龄": 18})
# text.writerow({"姓名": "红红", "年龄": 17})
# text.writerow({"姓名": "兰兰", "年龄": 16})


# import csv
# with open(r"c:\test3.csv", mode="a", newline="") as f1:
#     filedname = ["姓名", "年龄"]
#     text = csv.DictWriter(f1, filedname)
#     # 写表头
#     text.writeheader()
#     text.writerow({"姓名": "花花", "年龄": 18})
#     text.writerow({"姓名": "红红", "年龄": 17})
#     text.writerow({"姓名": "兰兰", "年龄": 16})







