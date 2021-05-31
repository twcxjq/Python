# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     py_bool
# Author:      TianChangJun
# Datetime:    2021/5/31 17:41
# Description：
# -----------------------------------------------------------------------------------

# 一般bool类型都是和条件判断语句或者循环语句结合使用
# 1.布尔型：True和False；
# 2.非空为True，空为False
#  True：非空字符串、非0的数字、计算结果为True的布尔表达式、非空列表、
#  非空元组、非空字典、非空集合、True等
# if 条件：  当条件满足（True）就执行语句体，不满足就不执行
#     语句体
if "nihao":
    print("柳暗花明又一村")
if 99:
    print("车到山前必有路")
if 1+1:
    print("船到桥头自然直")
if [2,5]:
    print("牧童遥指杏花村")
if True:
    print("借问酒家何处有")

#  False：0、None、空字符串、空列表、空元祖、空集合、空字典，False等
if 0:
    print("fsdfdsf")
if []:
    print("dfdfsdfsdf")
if "":
    print("fdfsdf")
if False:
    print("fdsfsdf")
"""

# if "a3" in "nihao":
#     print("在里面")
# else:
#     print("不在里面")



# 从键盘输入分数，获取应的评语
# num = int(input("请输入您的成绩："))
# if num>=0 and num<60:
#     print("成绩非常差，回家种田吧")
# elif num >= 60 and num < 70:
#     print("成绩一般，继续努力")
# elif num >=70 and num <80:
#     print("成绩还行，继续加油")
# elif num >=80 and num<90:
#     print("成绩良好，奖励棒棒糖")
# elif num>=90 and num<=100:
#     print("成绩优异，奖励一本练习题")
# else:
#     print("成绩无效")


# # 判断偶数还是奇数
# num = int(input("请输入一个数字："))
# if num%2 == 0:
#     print("偶数")
# else:
#     print("奇数")
#
# # 三元运算符 语法：结果值1 if bool表达式 else  结果值2。
# print("偶数" if num%2 == 0 else "奇数")
"""

for i in [1,2,3,4,5,6]:
    if i != 4:
        print(i)
else:
    print("取完了")



