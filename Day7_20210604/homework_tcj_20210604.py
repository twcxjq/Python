# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     homework_tcj_20210604
# Author:      TianChangJun
# Datetime:    2021/6/5 0:52
# Description：
# -----------------------------------

import os

"""
1,os和io操作：
    判断是否存在文件夹c:\\hello,
        存在则判断c:\\hello中是否有test.txt文件,有则把文件内容打印出来，
        没有则创建文件，并且获取c盘下所有的文件和目录名称写入到文件中；
    不存在则创建文件夹c:\\hello
"""

while 1:
    if os.path.isdir(r"c:\hello"):
        if os.path.isfile(r"c:\hello\test.txt"):
            with open(r"c:\hello\test.txt") as f1:
                data_test = f1.read()
                print(data_test)
                break
        else:
            with open(r"c:\hello\test.txt", mode="a") as f2:
                # 获取指定目录下所有的目录和文件
                data_file_dir = os.listdir(r"c:\\")   # 以列表形式返回数据
                for item in data_file_dir:
                    f2.write(item + "\n")  # write()方法的参数需要传入字符串str
            print("已创建test.txt文件")
    else:
        os.mkdir(r"c:\hello")
        print("已创建hello文件夹")


"""
2,定义全局变量：用两个函数去调用，并且把小白鞋（全局变量）， 用global修改为红色高跟鞋，然后输出
"""
