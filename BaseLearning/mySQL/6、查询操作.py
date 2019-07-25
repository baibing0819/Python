#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: 6、查询操作.py
@time: 7/11/19 11:00 AM
@desc:
'''

'''

fetchone()
func:  获取下一个查询结果集，结果集是一个对象

fetchall()
func:接受全部返回的行

rowcount:是一个只读属性，返回execute()方法影响的行数

'''

import  pymysql

#连接数据库,arg1:mysql主机ip，arg2:用户名 ,arg3:密码  arg4 : 数据库名
db = pymysql.connect("localhost","root","bai950915","test")

#创建一个cursor对象
cursor =db.cursor()

sql = 'select * from bankcard where money<300'
try:
    cursor.execute(sql)

    reslist = cursor.fetchall()
    for row in reslist:
        print("%d--%d"%(row[0],row[1]))

except:
    #如果提交失败，回滚到上一次数据
    db.rollback()

cursor.close()  #断开连接
db.close()