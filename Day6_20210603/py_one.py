# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     py_one
# Author:      TianChangJun
# Datetime:    2021/6/3 11:36
# Description：
# -----------------------------------------------------------------------------------

import random
import string

# 生成一个随机数
num = random.randint(1, 100)
print(num)
xing = ["赵", "钱", "孙", "李"]
ming = ["小强", "小花", "兰兰", "小号"]

name = random.choice(xing)+random.choice(ming)
print(name)
print(string.digits)
print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.ascii_letters)

print("".join(random.sample(string.ascii_letters+string.digits, 16)))

for i in range(1, 7):
    name1 = random.choice(xing)+random.choice(ming)
    pwd = "".join(random.sample(string.ascii_letters+string.digits, 16))
    print("用户名:{},密码:{}".format(name1, pwd))
