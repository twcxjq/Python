# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     homework_tcj_20210604
# Author:      TianChangJun
# Datetime:    2021/6/5 0:52
# Description：
# -----------------------------------

import os
import string

"""
1,os和io操作：
    判断是否存在文件夹c:\\hello,
        存在则判断c:\\hello中是否有test.txt文件,有则把文件内容打印出来，
        没有则创建文件，并且获取c盘下所有的文件和目录名称写入到文件中；
    不存在则创建文件夹c:\\hello
"""

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
                data_file_dir = os.listdir(r"c:\\")  # 以列表形式返回数据
                for item in data_file_dir:
                    f2.write(item + "\n")  # write()方法的参数需要传入字符串str
            print("已创建test.txt文件")
    else:
        os.mkdir(r"c:\hello")
        print("已创建hello文件夹")
"""

"""
2,定义全局变量：用两个函数去调用，并且把小白鞋（全局变量）， 用global修改为红色高跟鞋，然后输出
"""

"""
girl_shoes = "小白鞋"


class Showes:
    def shoes_1(self, species_1):
        print("{}是{}的最爱".format(girl_shoes, species_1))

    def shoes_2(self, species_2):
        global girl_shoes
        girl_shoes = "红色高跟鞋"
        print("{}是{}最喜欢的".format(girl_shoes, species_2))


if __name__ == '__main__':
    shoes = Showes()
    shoes.shoes_1("男生")
    shoes.shoes_2("女生")
    print(girl_shoes)
"""

"""
3,实现如下逻辑
    从键盘输入小花的python期末成绩。
    当成绩为100分时，奖励一张出游机票；
    当成绩为[80-99]时，奖励一个iphone；
    当成绩为[60-79]时，奖励一本参考书；
    其它时，什么奖励也没有
4,把第3题封装成一个类中的一个方法
"""

"""
class GradeReward:
    def reward(self):
        while True:
            input_grade = input("请输入Python期末成绩:")
            if input_grade.isdigit() and (int(input_grade) >= 0 and int(input_grade) <= 100):
                break
        grade = int(input_grade)
        if grade == 100:
            print("你的成绩是{},奖励一张出游机票".format(grade))
        elif grade >= 80 and grade <= 99:
            print("你的成绩是{},奖励一个iphone".format(grade))
        elif grade >= 60 and grade <= 79:
            print("你的成绩是{},奖励一本参考书".format(grade))
        else:
            print("你的成绩是{},对不起,什么奖励也没有".format(grade))


if __name__ == '__main__':
    gradeReward = GradeReward()
    gradeReward.reward()
"""

"""
5,完成以下图形的输出
"""

"""
class PrintGraphics:
    def Graphics(self, total):
        for item in range(1, total + 2):
            if item != total + 1:
                print("*" * item)
            else:
                item -= 1
                while (item > 0):
                    item -= 1
                    print("*" * item)

if __name__ == '__main__':
    printGraphics = PrintGraphics()
    printGraphics.Graphics(5)
"""

"""
6,一口缸容量有180升，一个和尚每次挑水20升，约多少次挑满？
"""

"""
capacity = 180
aTime = 20
count = 0
while capacity > 0:
    count += 1
    capacity -= aTime
    print("挑了{}次，水缸中的水有{}升了".format(count, count * aTime))
else:
    print("一口缸容量有{}升，一个和尚每次挑水{}升，约{}次挑满".format(count * aTime, aTime, count))
"""

"""
7, 去掉重复的内容  list2 = [1,2,3,1,2,3]
"""

"""
list2 = [1, 2, 3, 1, 2, 3]
print("这是列表list2:", list2)
set_list2 = set(list2)
print(type(set_list2), set_list2)
print("这个集合set_list2:", set_list2)
list_set_list2 = list(set_list2)
print(type(list_set_list2), list_set_list2)
print("这是列表list_set_list2:", list_set_list2)
"""

"""
8, 请用列表推导式输出
    1、list3 = [1,4,9,16,25,36,49,64,81,100]
    2、list4 = [81,100]
    3、再通过list3得到：list5 = [1,9,25,49,81]
"""

"""
list3 = [item ** 2 for item in range(1, 11)]
print(list3)
list4 = [item ** 2 for item in range(9, 11)]
print(list4)
list5 = [item for item in list3 if item % 2 != 0]
print(list5)
"""

"""
9, s = "bcdabcdabcdabcda"，去重并从小到大排序输出"abcd"
"""

"""
s = "bcdabcdabcdabcda"
set_s = set(s)
list_set_s = list(set_s)
list_set_s.sort()
str1 = "".join(list_set_s)
print(str1)
"""

"""
10, 字典根据键从小到大排序
    dict1={"name":"张三","age":18,"city":"成都","like":"篮球"}
    结果如图：排序后为dict2
    并交换新字典里面的k和v的值，如图
"""

"""
dict1 = {"name": "张三", "age": 18, "city": "成都", "like": "篮球"}
dict2 = {}
list_k_first = []
for k, v in dict1.items():
    list_k_first.append(k[0])
list_k_first.sort()
for item in list_k_first:
    for k, v in dict1.items():
        if item == k[0]:
            dict2[k] = v
print("排序前:", dict1)
print("排序后:", dict2)
print("交换k和v之前:", dict2)
print("交换k和v之后:", {v: k for k, v in dict2.items()})
"""

"""
11，列表推导式求list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]列表中所有奇数并构造一个新列表:[1,3,5,7,9]
"""

"""
list1 = [item for item in range(1, 11)]
list2 = [item for item in list1 if item % 2 != 0]
print(list2)
"""
