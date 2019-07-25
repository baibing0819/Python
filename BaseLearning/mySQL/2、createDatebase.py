#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: createDatebase.py
@time: 7/11/19 10:48 AM
@desc:
'''

import  pymysql

#连接数据库,arg1:mysql主机ip，arg2:用户名 ,arg3:密码  arg4 : 数据库名
db = pymysql.connect("localhost","root","bai950915","test")

#创建一个cursor对象
cursor =db.cursor()

#检查表是否存在，如果存在则删除
cursor.execute("drop table if exists bankcard")

sql = 'create table bankcard(id int auto_increment primary key ,money int not null)'
cursor.execute(sql)

cursor.close()  #断开连接
db.close()