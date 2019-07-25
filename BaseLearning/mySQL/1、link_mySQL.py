#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: 1、link_mySQL.py
@time: 7/11/19 10:39 AM
@desc:
'''

import  pymysql

#连接数据库,arg1:mysql主机ip，arg2:用户名 ,arg3:密码  arg4 : 数据库名
db = pymysql.connect("localhost","root","bai950915","test")

#创建一个cursor对象
cursor =db.cursor()

sql = "select version()" #要执行的sql语句

cursor.execute(sql)   #执行

data = cursor.fetchone()  #获取返回的信息
print(data)

cursor.close()  #断开连接
db.close()