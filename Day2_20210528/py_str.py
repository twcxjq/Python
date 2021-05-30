# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     py_str
# Author:      TianChangJun
# Datetime:    2021/5/28 16:44
# Description：字符串是Python 中最常用的数据类型。我们可以使用引号( ' 或 " )来创建字符串
#-----------------------------------------------------------------------------------

# 创建一个空字符串
str1 = "";
str2 = "";

# 查看字符串长度 len(对象)
print(type(str1),len(str1));
print(type(str2),len(str2));

# 定义一个非空字符串
str3 = "hello_python";
print(type(str3), len(str3));
print(str3);

# 单独把e拿出来
print(str3[1]);   # 下标索引从0开始

# 拿一部分python
# 切片: 格式: str[起始下标索引:终止下标索引:步长]
# 起始值不写默认从第一个元素开始，终止值不写默认。默认取到最后，步长不写默认为1
# 区间左闭右开
print(str3[6:]);
print(str3[6:13]);  #超过最大下边索引,不报错,默认取到最后
print(str3[2:5]);

str4 = "123456789";
# 取13579
print(str4[::2]);
# 取结果为:987654321
print(str4[::-1]);    # 反转字符串
# 取765
# 步长为正，从左往右取，下标索引从0开始
# 步长为负，从右往左取，下标索引从-1开始
print(str4[-3:-6:-1]);
print(str4[-1:]);   # 9
print(str4[-1]);   # 9
print(str4[-1::]);   # 9
print(str4[0:]);   # 123456789
print(str4[0::]);   # 123456789
print(str4[0]);   # 1

# 取1234hello
print(str4[:4]+str3[:5]);

str5 = "hello";
print(str5[4]);
# print(str5[5]);   #IndexError: string index out of range
print("str5[3:1000]:", str5[3:1000]);

str_in = "hello";
str_in1 = "123456ll";
print("ll" in str_in);  #True
print("ll" in (str_in, str_in1));  #False   判断"ll"是否为str_in或者str_in1
print("hello" in (str_in, str_in1));  #True   判断"ll"是否为str_in或者str_in1
# 注意：如果是想比较两个字符串是否相等，还是需要用 == 或者 !=

str6 = "hello_112345";
print("23" in str6);
# 统计出现的次数
print(str6.count("l"));
print(str6.count("1", 4, 8)); # 查找指定索引范围内的次数

str7 = "helloee_12eeeeeee45";
print(str7.find("e"));  #只返回第一个索引位置
print(str7.find("fdsags")); #如果不存在，返回-1
print(str7.find("e", 3, 77)); #返回索引范围内的第一个索引位置
print(str7.find("e4")); #利用唯一性来查看你索引位置

print(str7.index("e"));
print(str7.index("e", 3, 99));
# print(str7.index("e121", 3, 99)); # ValueError: substring not found

# 分割之后的元素在存在在列表中的
str8 = "hello,python";
# print(str8.split("_"));
print(str8.split("o"));

str9 = "你好";
str10 = "hello+python";

print("钱".join(str9));
print(str9.join(str10));
print("o".join(str10));

print("hello".startswith('he'));
print("hello".endswith("o"));

str11 = "Hello";
print(str11.upper());
print(str11.lower());
print(str11.isupper());
print(str11.islower());

print("123a".isalnum());
print("123".isalpha());
print("123".isdigit());

'''
if input("请输入你的密码: ").isdigit():
    print("你的密码过于简单，请重新输入！");
else:
    print("非纯数字");
'''

str12 = "this is a beautiful girl";
print(str12.capitalize()); # 返回第一个单词首字母大写

# 返回"标题化"的字符串,就是说所有单词的首字母都转化为大写
print(str12.title());  # 返回每个单词首字母大写
print(str12.istitle());
print(str12.title().istitle());

str13 = "afsadeadswAS";
print(str13.replace("a", "A"));
print(str13.replace("a", "A", 1));

#把str13中的第2个a替换成A
print(str13.replace("ad", "Ad", 1)) #（找唯一性替换）
print(str13.replace("ad", "Ad", 2).replace("Ad", "ad", 1)) #（找唯一性替换）

str14 = "nihao";
str15 = "laowang";

print(str14 + str15);
print(str14, str15);
print(str14.join(str15));
print(str14[:3] + "li");
print(str14*10);


























