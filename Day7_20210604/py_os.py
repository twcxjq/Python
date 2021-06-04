# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     py_os
# Author:      TianChangJun
# Datetime:    2021/6/4 10:31
# Description：
# -----------------------------------------------------------------------------------

import os

# 创建目录，只能创建一级新目录，如果存在，则无法创建
# os.mkdir(r"c:\hello1\h1")

# 删除空目录
# os.rmdir(r"c:\hello1\h1")

# 删除空目录(既可以删除空目录，也可以删除非空目录)
import shutil
# shutil.rmtree(r"c:\hello1")



# 判断文件夹是否存在(判断是否是文件夹)
print(os.path.isdir(r"c:\hello"))
# 判断文件是否存在(判断是否是文件)
print(os.path.isfile(r"c:\mingdan.txt"))
# 判断文件或者文件夹是否存在(判断是否是文件夹或者文件)
print(os.path.exists(r"c:\hello"))
print(os.path.exists(r"c:\mingdan.txt"))

# 打印平台信息 nt 表示win32
print(os.name)

import  sys
print(sys.platform)
# 打印id
print(os.getpid())
# 获取当前路径
print(os.getcwd())

# 路径拼接
path1 = os.getcwd()
path2 = "\py_os.py"
path3 = "py_os.py"
print(path1 + path2)
print(os.path.join(path1, path3))




