# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     py_io
# Author:      TianChangJun
# Datetime:    2021/6/4 11:28
# Description：
# -----------------------------------------------------------------------------------

import os

# 打印路径下所有的目录和文件(隐藏文件也列出)
for i in os.listdir(r"c:\\"):
    print(i)

# 打开文件
f1 = open(r"c:\text11.txt", mode="r")
# 读取内容
data = f1.read()
print(type(data), data)   # 字符串类型
f1.close()

# 创建文件mode=a(追加)或者mode=w(覆盖)表示创建文件
f2 = open(r"d:\text22.txt", mode="a")
f2.write(data + "\n")
f2.close()
