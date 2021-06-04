# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     py_practise
# Author:      TianChangJun
# Datetime:    2021/6/4 12:53
# Description：
# -----------------------------------------------------------------------------------

# import os
#
# # 判断c盘下是否有hello文件夹
# print(os.path.isdir(r"c:\hello"))
# # 如果没有则创建hello文件夹
# # os.mkdir(r"c:\hello")
# """
# 如果文件夹存在，就判断里面是否有test.txt这个文件，如果有就把里面的内容打印出来
# 如果没有就就创建文件并且输入静夜思
# """
# print(os.path.isfile(r"c:\hello\test.txt"))
#
#
#
# file_test1 = open(r"c:\hello\test.txt", mode="r")
# data1 = file_test1.read()
# if (data1 == ""):
#     file_test = open(r"c:\hello\test.txt", mode="w")
#     data = ["静夜思", "床前明月光", "疑是地上霜", "举头望明月", "低头思故乡"]
#     for i in data:
#         file_test.write(i + "\n")
#     file_test.close()
# else:
#     print(data1)
# file_test1.close()

import os

while 1:
    if os.path.isdir(r"c:\hello"):
        if os.path.isfile(r"c:\hello\test.txt"):
            file_test = open(r"c:\hello\test.txt", mode="r")
            print(file_test.read())
            file_test.close()
            break
        else:
            file_test1 = open(r"c:\hello\test.txt", mode="w")
            data = ["静夜思", "床前明月光", "疑是地上霜", "举头望明月", "低头思故乡"]
            for i in data:
                file_test1.write(i + "\n")
            file_test1.close()
    else:
        os.mkdir(r"c:\hello")
