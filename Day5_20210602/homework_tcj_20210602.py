# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     homework_tcj_20210602
# Author:      TianChangJun
# Datetime:    2021/6/2 15:08
# Description：
# -----------------------------------------------------------------------------------

"""
1、求列表里面所有数字(int)的和
list1 = [1,9,[2,8,[3,7]],(4,6),{1,9},{"姓名":"张三","年龄":10,2:8},"nihao"]
"""

# def list_int_sum(list_name):
#     sum_int = 0
#     for item in list_name:
#         if type(item) == int:
#             sum_int += item
#         elif type(item).__name__ == "list":
#             for item_list in item:
#                 if type(item_list) == int:
#                     sum_int += item_list
#                 if type(item_list) == list:
#                     for item_list_1 in item_list:
#                         if type(item_list_1) == int:
#                             sum_int += item_list_1
#         elif isinstance(item, tuple):
#             for item_tuple in list(item):
#                 if type(item_tuple) == int:
#                     sum_int += item_tuple
#         elif type(item) == set:
#             for item_set in list(item):
#                 if type(item_set) == int:
#                     sum_int += item_set
#         elif type(item) == dict:
#             for k, v in item.items():
#                 if type(k) == int:
#                     sum_int += k
#                 if type(v) == int:
#                     sum_int += v
#         elif type(item) == str:
#             continue
#     return sum_int
#
#
# if __name__ == '__main__':
#     list1 = [1, 9, [2, 8, [3, 7]], (4, 6), {1, 9}, {"姓名": "张三", "年龄": 10, 2: 8}, "nihao"]
#     print(list_int_sum(list1))


sum_int = 0


def list_int_sum(list_name):
    global sum_int
    wz = -1
    for item in list_name:
        wz += 1
        if type(item) == int:
            sum_int += item
        elif type(item).__name__ == "list":
            item_list_wz = -1
            for item_list in item:
                item_list_wz += 1
                if type(item_list) == int:
                    sum_int += item_list
                else:
                    list_int_sum(list(list_name[wz][item_list_wz]))
        elif isinstance(item, tuple):
            item_tuple_wz = -1
            for item_tuple in list(item):
                item_tuple_wz += 1
                if type(item_tuple) == int:
                    sum_int += item_tuple
                else:
                    list_int_sum(list(list_name[wz][item_tuple_wz]))
        elif type(item) == set:
            item_set_wz = -1
            for item_set in list(item):
                item_set_wz += 1
                if type(item_set) == int:
                    sum_int += item_set
                else:
                    list_int_sum(list(list_name[wz][item_set_wz]))
        elif type(item) == dict:
            for k, v in item.items():
                if type(k) == int:
                    sum_int += k
                else:
                    list_int_sum(list(k))
                if type(v) == int:
                    sum_int += v
                else:
                    list_int_sum(list(v))
        elif type(item) == str:
            continue
        else:
            pass
    return sum_int


if __name__ == '__main__':
    list1 = [1, 9, [2, 8, [3, 7]], (4, 6), {1, 9}, {"姓名": "张三", "年龄": 10, 2: 8}, "nihao"]
    # list1 = [1, 9, 10, [2, 10, 8, [3, 7, [3, 7]]], (4, 6, (1, 9)), {1, 9},
    #          {"姓名": "张三", "年龄": 10, 2: 8, (1, 9): "对的", "cc": [5, 5]}, "nihao"]
    print(list_int_sum(list1))

"""
2, 冒泡排序:
将list1 = [7, 4, 3, 67, 34, 1, 8]中的数据从小到大排序，最后输出结果为：[1, 3, 4, 7, 8, 34, 67]：
提示冒泡排序，比较大小交换位置，或者用空杯交换原理
"""


# def paixu(list_number):
#     list_len = len(list_number)
#     for count in range(0, list_len - 1):
#         for step in range(0, list_len - count - 1):
#             if list_number[step] > list_number[step + 1]:
#                 list_number[step], list_number[step + 1] = list_number[step + 1], list_number[step]
#     return list_number
#
#
# if __name__ == '__main__':
#     list1 = [7, 4, 3, 67, 34, 1, 8]
#     print(paixu(list1))


def paixu1(list_number):
    list_len = len(list_number)
    for count in range(0, list_len - 1):
        for step in range(0, list_len - count - 1):
            if list_number[step] > list_number[step + 1]:
                # list_number[step], list_number[step + 1] = list_number[step + 1], list_number[step]
                temp = list_number[step]
                list_number[step] = list_number[step + 1]
                list_number[step + 1] = temp
    return list_number


if __name__ == '__main__':
    list1 = [7, 4, 3, 67, 34, 1, 8]
    print(paixu1(list1))

"""
3、求1-2+3-4+5-6+7-8+9 ... 99的值
"""

# def jiajian(number):
#     if number == 99:
#         return 99
#     return number - jiajian(number + 1)
#
#
# if __name__ == '__main__':
#     print(jiajian(1))
#
#
# def jiajian1(start_num, stop_num):
#     sum_num = 0
#     for item  in range(start_num, stop_num):
#         sum_num += (-1) ** (item + 1) * item
#     return sum_num
#
#
# if __name__ == '__main__':
#     print(jiajian1(1, 100))
