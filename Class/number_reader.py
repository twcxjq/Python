# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     number_reader
# Author:      TianChangJun
# Datetime:    2021/6/5 17:23
# Description：
# -----------------------------------------------------------------------------------

import json

filename = "numbers.json"
with open(filename, mode="r") as f_obj:
    numbers = json.load(f_obj)

print(numbers)
