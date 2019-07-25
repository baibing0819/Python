#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: 5、deleteData.py
@time: 7/11/19 10:57 AM
@desc:
'''


import  pymysql

#连接数据库,arg1:mysql主机ip，arg2:用户名 ,arg3:密码  arg4 : 数据库名
db = pymysql.connect("localhost","root","bai950915","test")

#创建一个cursor对象
cursor =db.cursor()

sql = 'delete from bankcard where money=100'
try:
    cursor.execute(sql)
    db.commit()   #插入数据后必须提交才生效
except:
    #如果提交失败，回滚到上一次数据
    db.rollback()

cursor.close()  #断开连接
db.close()