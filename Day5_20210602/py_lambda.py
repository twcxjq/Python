# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     py_lambda
# Author:      TianChangJun
# Datetime:    2021/6/2 11:45
# Description：
# -----------------------------------------------------------------------------------

"""
方法1：将整个函数用括号括起来，在后面再使用括号传入实参调用，
如果没有实参也需要带上括号表示执行该匿名函数，
否则返回的是该匿名函数的对象；如(lambdax,y:x+y)(4,22)

方法2：讲lambda函数赋值给变量，然后像普通函数那样调用；如
a=lambda x,y:x+y
a(4,22)
"""

add = lambda a, b: a + b

print(add(3, 2))

print((lambda a, b: a + b)(2, 3))
print((lambda a: a)(9))
