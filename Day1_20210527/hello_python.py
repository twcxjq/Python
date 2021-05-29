# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     hello_python
# Author:      TianChangJun
# Datetime:    2021/5/27 15:34
# Description：
# -----------------------------------------------------------------------------------

# print("你好,Python");

'''
# 导入模块/库
import keyword

# 第一个函数,用于输出内容
print(keyword.kwlist);  # 调用对象的方法是用对象.方法名
for i in keyword.kwlist:
    print(i);
'''

# print("静夜思","李白");

# 打印内容不换行,字符串类型:只要是引号引起来的都是字符串
# print("静夜思",end="");
# print("窗前明月光");

# 打印换行
# print("-静夜思-\n","窗前明月光\n","疑似地上霜\n","低头望明月\n","低头思故乡");
# print("-静夜思-","\n窗前明月光","\n疑似地上霜","\n低头望明月","\n低头思故乡");

# 重复打印一个对象
# print("你好" * 6);

'''
# 输入函数: input()从键盘输入内容,类型都是字符串类型
num = int(input("请输入您的支付宝密码:"));
if num > 100:
    print("你好");
else:
    print("不太好");
'''

'''
# 什么是变量
#变量赋值
name = "小花"; #赋值字符串
age = 99; #赋值int
money = 1000.00;  #赋值float
add = 1 + 1;  #赋值运算表达式
booll = 33 > 8  or 44 < 9 and 3 > 8
print(name);
print(age);
print(money);
print(add);
print(booll);

a,b,c = 1,2,3;
print(a);
print(b);
print(c);

d = f = g = 88;
print(d);
print(f);
print(g);

aa = 99;
bb = 100;
#交换aa与bb的值
aa,bb = bb,aa;
print(aa);
print(bb);
'''

"""
# 把对象转换成整型  int(对象名)
# 把对象转换成字符串类型  str(对象名)
# 格式化输出
name = "小花";
age = 99;
height = 168;
# %s 格式化字符串，也可以格式化数值
print("老王喜欢" + name);
print("老王喜欢%s,今年%d岁了"%(name,age));
print("老王喜欢%s,今年%s岁了"%(name,age));
# %d 格式化整数
print("老王喜欢",name,"今年",age,"岁了");
print("老王喜欢" + name + "今年" + str(age) + "岁了");
print("老王喜欢%s,今年%s岁了,身高%d"%(name,age,height));
# %f 格式化浮点数,可指定小数点后的精度 3.1415926
import math

print("pi的近似值是%f"%math.pi);
print("pi的近似值是%5.3f"%math.pi);
print("pi的近似值是%5.30f"%math.pi);
print("pi的近似值是%50.3f"%math.pi);
print("pi的近似值是%050.3f"%math.pi);
print("pi的近似值是%33f"%math.pi);
print("pi的近似值是%-50.3f"%math.pi);
print("pi的近似值是%-50.300f"%math.pi);

name1 = "小花";
age1 = 99;
color1 = "绿色";
print("老王喜欢{},今年{}岁了,头发颜色是{}".format(name1,age1,color1));
print("老王喜欢{0},今年{1}岁了,头发颜色是{2}".format(name1,age1,color1));  #索引从0开始
print("老王喜欢{name},今年{age}岁了,头发颜色是{color}".format(name = name1,age = age1,color = color1));
"""

#sep:插入值之间的字符串，默认为空格
print("a","b",sep='-');

#end:附加在最后一个值之后的字符串，默认为换行符（\n）
print("a",end="--");
print("b");

# 当%和format同时使用时，因为str.format(),所以format必须放在前面,%跟在format后面
print("老王喜欢%s,今年%d了，头发颜色是{},喜欢{}".format("绿色","篮球")%("小花",99));



