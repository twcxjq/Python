# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     py_num
# Author:      TianChangJun
# Datetime:    2021/5/28 10:28
# Description：
#-----------------------------------------------------------------------------------

"""
import decimal

a = 6.1;
# decimal一般在做精确计算时使用
b = decimal.Decimal(6.1);
print(a);
print(b);
"""
"""
# complex() 创建复数
print(complex("3"));
print(complex("3"));
print(complex(3+2)); #表达式是将计算结果赋值给实部
print(complex("3+2j")); #字符串是分别赋值给实部和虚部，虚部必须带单位j,+前后不能有空格
print(complex(3+2j)); #字符串是分别赋值给实部和虚部，虚部必须带单位j,+前后不能有空格
print(complex("3j"));
print(complex(2,3j)); #2-3的结果赋值给实部，虚部为0
"""

# a = 2;
# b = 3;
# print("a + b = {}".format(a + b));
# print("a - b = {}".format(a - b));
# print("a x b = {}".format(a * b));
# print("a / b = {}".format(a / b));
# print("a % b = {}".format(a % b));
# print("a // b = {}".format(a // b));
# print("a ** b = {}".format(a ** b));

"""
a,b,c = 2,4,6;
print(a > b);
print(b < c);
print(a <= c);
print(c >= 6);
print(c != a);
print(4 == 4); # =表示赋值，==表示等于 判断

print(c > 3 and b < 1);
print(c > 3 or b < 1);
print(c > 3 or b < 1 and 4 >= 89);  #先算and，再算or

print(not a > 5);
"""

'''
a = 0b1010;
b = 0b1000;
# a为一个二进制数，但打印出来是十进制数（在python中数据默认是十进制数）
print(a);
print(0o1010);
print(0x1010);

# 十进制-->二进制
print(bin(8));
# 八进制-->二进制
print(oct(8));
# 十六进制-->二进制
print(hex(8));

# int(x,base=y)：表示把y进制的字符串x转换成十进制的整数
print(int("0b1010",base=2));
'''

"""
a=0b1010;
b=0b1011;
print(a,b);

# 1&1结果是1, 1&0结果是0, 0&1结果是0,0&0结果还是0；与运算，只要有0 就是0
print(bin(a&b));
print(a&b);

# 1|1结果是1, 1|0结果是1, 0|1结果是1,0|0结果是0；或运算，只要有1  就是1
print(bin(a|b));
print(a|b);

#0跟任意数做与 运算，结果都是0, 0跟任意数做 或 运算，结果取决于对方
print(99999&0);     #输出0
print(99999|0);    #输出99999

# 异或：相同则为0，不同则为1，比如1^0结果是1，1^1结果是0，0^0结果是0
print(bin(a^b));
print(a^b);

# 非：~1结果是0，~0结果是1         加1取反
print(bin(~a));
print(~a);
print(a);

# 左移n位，相当于乘以2的n次方（在不溢出的前提下），右移n位，相当于除以2的n次方（得到的是整数）
print(bin(a<<3));
print(a<<3);
print(bin(b>>2));
print(b>>2);
"""

"""
print("45" in "12345");
if "52" in "123456":
    print("在里面");
else:
    print("不在里面");

for i in "123456":
    print(i);

print("3" not in "123");
"""

"""
a = "123qwe!@#";
b = "123qwe!@#";
print(a is b);
print(a is not b);
print(a == b);
print(a != b);

# 判断对象的内存地址
# 获取对象的内存地址 id(对象名)
# 变量a与变量b的内存地址是不一样的（即两个变量引用的对象不是同一个对象），
# 这里是因为pycharm做了一次内存优化,使得两个变量引用的对象是同一个对象
print(id(a));
print(id(b));
print(id(a) is id(b));
print(id(a) == id(b));
print(id(a) is not id(b));
print(id(a) != id(b));
"""

num = 99;
# 类型并不都是可以随意转换的
# 查看对象类型 type(对象名)
print(type(num));
a = str(num);  #把int转换为str
print(type(a));

name = "66";
print(type(name));
b = int(name);  #非数字的字符串是不能转换为整型的
print(type(b));
height = "180cm"  #不能转换为int或者float
















