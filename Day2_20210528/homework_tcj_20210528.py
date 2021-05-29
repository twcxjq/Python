# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     homework_tcj_20210528
# Author:      TianChangJun
# Datetime:    2021/5/28 23:04
# Description：
# -----------------------------------

# 1,根据给出的数据,请用转义字符进行如下格式的输出
s = 'Hello\nStudents\nGood\nMorning';
s2 = '商品名\t单价\t数量\t总价';
s3 = '皮鞋\t99\t\t2\t\t198';
s4 = '大衣\t108\t\t10\t\t1080';

print(s + "\n" + s2 + "\n" + s3 + "\n" + s4);

# 2、给一个字符串str1 = "nihao,pengyou"   要求输出为：“nihao,peNgyou”  并找出N的位置，并统计出o出现的次数
str1 = "nihao,pengyou";
print("替换前: " + str1);
str2 = str1.replace("ng", "Ng");
print("替换后: " + str2);

print("N的索引位置是: {}".format(str2.find("N")));
# print("N的索引位置是: {}".format(str2.find("Ng")));  #利用唯一性查看元素的索引位置

print("o出现的次数为:", str2.count("o"));

# 3、给一个字符串：str3 = “zhouliu”, 要求输出为："ZHOULIU"
str3 = "zhouliu";
print("转换前: %s" % (str3));
print("转换后: %s" % (str3.upper()));

# 4、把 * 拼接到第3题的对象中
str4 = "*";
print("拼接前: " + str3);
print("拼接后1: " + str3 + str4);
print("拼接后2:", str3, str4);
print("拼接后3:", str4.join(str3));
print("拼接后4: " + str3[::] + str4);

'''
5、已知字符串"ronghuanettest@vip.com"，
要求对字符串进行切片操作，切片得到的每个字符串以列表返回，
最终结果是：["rong","hua","net","test","vip","com"]
'''
str5 = "ronghuanettest@vip.com";
str_result = [];
str_result.extend([str5[:4], str5[4:7], str5[7:10], str5[10:14], str5[15:18], str5[19:]]);
print(str_result);

"""
6、 一个列表list1=[1,1,1,1,1,1,10,11]；
 (a)统计该列表中出现1元素几次；
（b）反转列表
（c）要求在倒数第二个1前面添加一个元素列表list2=[2,3,4,2,1]，并输出添加后的列表
（d）删除第3个1
"""
list1 = [1, 1, 1, 1, 1, 1, 10, 11];
count_1 = list1.count(1);
print("该列表中出现1元素%d次" % (count_1));

print("反转前:", list1);
list1.reverse();
print("反转后:", list1);

list2 = [1, 1, 1, 1, 1, 1, 10, 11];
list2_fz = list2[::-1];
print("反转后:", list2_fz);

list3 = [1, 1, 1, 1, 1, 1, 10, 11];
list4 = [2, 3, 4, 2, 1];
list3.insert(-4, list4);
print("插入列表元素后的列表为:", list3);

list5 = [1, 1, 1, 1, 1, 1, 10, 11];
list6 = [2, 3, 4, 2, 1];
list5.insert(4, list6);
print("插入列表元素后的列表为:", list5);

list7 = [1, 1, 1, 1, 1, 1, 10, 11];
print("删除前:", list7);
list7.pop(2);
print("删除后:", list7);
