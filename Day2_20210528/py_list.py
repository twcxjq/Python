# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     py_list
# Author:      TianChangJun
# Datetime:    2021/5/30 15:09
# Description：标志 [] 有序的：可以用索引
#-----------------------------------

"""
# 创建一个空列表
list1 = [];
print(type(list1), len(list1));

# 创建一个空列表
list2 = [1, 2, 3, 4, 5, "你好", [99, 88, 66]];
print(type(list2), len(list2));

if type(list2) == list:
    print("是列表");
if type(list2).__name__ == "list":
    print("是列表");

# 如果要判断两个类型是否相同推荐使用 isinstance()
# type() 不会认为子类是一种父类类型，不考虑继承关系。
# isinstance() 会认为子类是一种父类类型，考虑继承关系
print(isinstance(list2, list));


# 练习题
list3 = [1, 2, 3, 4, 5, "你好", [99, 88, 66]];
# 遍历打印列表中的所有值，用循环
for item in list3:
    print(item);

# 只打印列表中2的值(1，用以前方法，2，用下标索引)
for item in list3:
    if item == 2:
        print(item);

print(list3[1]);

# 修改列表中第一个值为5
print("修改前: ", list3);
list3[0] = 5;
print("修改后: ", list3);

# 设计到比较的都是同一类型
list4 = [1, 2, 3, 4];
print(min(list4));
print(max(list4));

list5 = ["hello", "bool", "x", "A"];
print(min(list5));  # 按ASCII码进行比较
print(max(list5));

list6 = ["乔峰", "虚竹", "刘珊"];
print(min(list6));  # 按汉字的编码方式(base 10,GBK,UTF-8等)进行比较
print(max(list6));
"""

"""
# 类型转换
num = 2;
name = "小花";
list1 = [44, 7];
# print(list(num));    #TypeError: 'int' object is not iterable
# list(seq),seq为要转换为列表的元组或字符串。
print(list(name));
aa = str(list1);
print(aa);
print(type(aa));
"""

"""
list7 = [3, 5, 8, 9];
print("添加前:", list7);
list7.append(6); # 在末尾添加一个元素6
print("添加后:", list7);

print("添加前:", list7);
# list.extend(seq)：在列表末尾一次性追加另一个序列中的多个值
list7.extend([11, 12, 13]); # 在末尾添加序列(list)中的多个元素
print("添加后:", list7);

print("添加前:", list7);
# list.insert(索引位置,元素)：将元素插入列表的指定位置
list7.insert(1, 999); # 在指定索引位置添加一个元素
print("添加后:", list7);

# list.index(seq)：从列表中找出某个值第一个匹配项的索引位置
print(list7.index(999));
# print(list7.index(9999));   # ValueError: 9999 is not in list

list8 = [3, 5, 8, 9];
print("删除前:", list8);
# list.pop()：删除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print(list8.pop());
print("删除后:", list8);

# print("删除前:", list8);
# print(list8.pop(1));   # 删除第二个元素
# print("删除后:", list8);

# list.remove(元素)
# 删除列表中某个值的第一个匹配项，没有返回值
print("删除前:", list8);
list8.remove(3);
print("删除后:", list8);

# del list[索引]：删除索引位置元素
print("删除前:", list8);
del list8[0];
print("删除后:", list8);

print("删除前:", list8);
del list8;   # 删除整个列表
print("删除后:", list8);
"""


# 对原列表进行排序,列表可以为数字列表，也可以为字母列表，但是不能混合
# 默认为升序排序，降序排序修改reverse 参数为True
# list9 = [55, 99, 3, 5, 8, 9];
list9 = ["c", "b", "g", "w", "a"];
print("排序前:", list9);
# list9.sort();
list9.sort(reverse = True);
print("排序后:", list9);

# list.count(元素)：统计某个元素在列表中出现的次数，返回统计的次数
list10 = ["a", "a", "d"];
print(list10.count("a"));


# list.reverse()：反向列表中元素
list11 = [1,32,45,7,"d"];
print("反转前:", list11);
list11.reverse();
print("反转后:", list11);
bb = list11[::-1];
print("反转后:", bb);

# list.clear()：清空列表
list12 = [1, 2, 3];
print("清空前:", list12);
list12.clear();
print("清空后:", list12, "不好意思，前面列表中的元素已被清空, 只剩下一个空列表啦");

# list.copy()：复制列表
list13 = [1,2];
list_copy = list13.copy();
print(list_copy);

list14 = [1, 2, 3, 4, 5, 6];
list15 = [55, 22, 66, 88, 21];
print(list14 + list15);
print(list14, list15);
print(list14*3);

list16 = [1, 2, [4, 5, 6, [7, 8, 9]]];
# 要求把9改成10
print("修改前: ", list16);
print(list16[2]);
print(list16[2][3]);
print(list16[2][3][2]);
list16[2][3][2] = 10;
print("修改后: ", list16);



