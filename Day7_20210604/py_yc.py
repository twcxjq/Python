# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     py_yc
# Author:      TianChangJun
# Datetime:    2021/6/4 14:38
# Description：
# -----------------------------------------------------------------------------------

# 格式一
# try...except:当try的代码正常，不执行except,当try的代码异常才会执行except
# try:
#     print("进入try")
#     f1 = open(r"c:\mingdan.txt")
#     print("结束try")
# except FileNotFoundError as e:
#     print("进入except")
#     print(e)
#     print("结束except")

# 格式二
# try...except...else:当try的代码正常，不执行except,但是会执行else,当try的代码异常会执行except,但不执行else
# try:
#     print("进入try")
#     f1 = open(r"c:\mingdan.txt")
#     print("结束try")
# except FileNotFoundError as e:
#     print("进入except")
#     print(e)
#     print("结束except")
# else:
#     print("进入else")
#     f1.close()
#     print("结束else")

# 格式三
# try...finally:不管try的代码是否正常，都会执行finally的代码
# try:
#     print("进入try")
#     f1 = open(r"c:\mingdan.txt")
#     f2 = open(r"c:\mingdan1.txt")
#     print("结束try")
# finally:
#     print("进入finally")
#     f1.close()
#     print("结束finally")

# 格式四
# try...except...finally:当try的代码正常，不执行except,但是会执行finally的代码
# 当try的代码异常，会执行except,也会执行finally的代码
# try:
#     print("进入try")
#     f1 = open(r"c:\mingdan.txt")
#     f2 = open(r"c:\mingdan1.txt")
#     print("结束try")
# except FileNotFoundError as f:
#     print("进入except")
#     print(f)
#     print("结束except")
# finally:
#     print("进入finally")
#     f1.close()
#     print("结束finally")

# 格式五
# try...except:当try的代码正常，不执行except,当try的代码异常才会执行except
# try:
#     print("进入try")
#     f1 = open(r"c:\mingdan.txt")
#     f2 = open(r"c:\mingdan1.txt")
#     print("结束try")
# except:
#     # raise 自动引发异常
#     raise FileNotFoundError("请检查路径是否正常!!!")


user = input("请输入你的密码:")
try:
    print("你的密码是%d" % user)
    f1 = open(r"c:\mingdan.txt")
    f2 = open(r"c:\mingdan1.txt")
    print("结束try")
except TypeError as t:
    print(t)
    # raise 自动引发异常
    raise FileNotFoundError("请输入相对应的类型!!!")
