# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     homework_tcj_20210527
# Author:      TianChangJun
# Datetime:    2021/5/27 17:45
# Description：
# -----------------------------------------------------------------------------------

'''
打印一首歌（歌词），练习不同的注释方法和快捷键方法
'''
# 歌名
lyrics_name = "两只老虎\n";
# 作者
lyrics_author = "\tTCJ";
# 这是一个关于歌词的列表
lyrics_list = ['两只老虎', '跑的快', '一只没有眼睛', '一只没有耳朵', '真奇怪'];
print(lyrics_name, lyrics_author);
for item in lyrics_list:
    print(item);

print("-" * 50);
"""
给出数据:
星期1到星期7，天气为晴天，阴天，雨天，雾天，冰雹天，狂风暴雨天，雷电交加天，
老王分别要在这7天做7件事（事情个人自定义）
用格式化（%s %d）和.format()函数 的输出方式把这7天的内容输出：如：星期1，天气为晴天，老王今天要去游泳！
"""
day_of_week_list = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期天'];
weather_list = ['晴天', '阴天', '雨天', '雾天', '冰雹天', '狂风暴雨天', '雷电交加天'];
things_list = ['1学习Python', '2学习Python', '3学习Python', '4学习Python', '5学习Python', '6学习Python', '7学习Python'];
num_list = [0, 1, 2, 3, 4, 5, 6];

for num in num_list:
    print("%s,天气为%s，老王今天要去%s" % (day_of_week_list[num], weather_list[num], things_list[num]));

print("-" * 50);
for num in num_list:
    print(
        "{day_of_week},天气为{weather}，老王今天要去{things}".format(day_of_week=day_of_week_list[num], weather=weather_list[num],
                                                           things=things_list[num]));
