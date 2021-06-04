# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     py_mysql
# Author:      TianChangJun
# Datetime:    2021/6/3 17:12
# Description：
# -----------------------------------------------------------------------------------

"""
# 读取数据库数据

import pymysql

my_connect = pymysql.connect(host="106.13.199.209", user="root", password="ronghuanet@2019",
                             database="message", port=3306, charset="utf8")
#创建游标，作用是便利所有的数据存放到游标中，以便后面操作
youbiao = my_connect.cursor()
# #执行SQL语句
youbiao.execute("select * from tbl_sms_plan where id=100;")
# 获取执行后的数据
data = youbiao.fetchall()  #返回元组类型的数据
print(data[0])
print(data[0][0])
#关闭数据库与游标
my_connect.close()
youbiao.close()
"""


# 修改数据库数据

import pymysql

my_connect = pymysql.connect(host="106.13.199.209", user="root", password="ronghuanet@2019",
                             database="message", port=3306, charset="utf8")
#创建游标，作用是便利所有的数据存放到游标中，以便后面操作
youbiao = my_connect.cursor()
#执行SQL语句
youbiao.execute("INSERT INTO tbl_sms_plan (id,NAME,company_id,TYPE,STATUS,create_dt,update_dt) VALUES (100,'29期_田昌君',1997,1,1,NOW(),NOW());")
#提交数据
my_connect.commit()
# 获取执行后的数据
youbiao.execute("select * from tbl_sms_plan where id=100;")
data = youbiao.fetchall()
print(data[0])
#关闭数据库与游标
my_connect.close()
youbiao.close()

