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

