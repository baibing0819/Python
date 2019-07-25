#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: 1、添加文档.py
@time: 7/11/19 5:54 PM
@desc:
'''

from pymongo import MongoClient


#连接服务器
conn = MongoClient("localhost",27017)

#连接数据库
db = conn.mydb

#获取集合
collection = db.student

#添加文档
collection.insert({"name":"白贼帅","age":18,"gender":1,"address":"深圳","isDelete":0})
#最新推荐使用insert_one insert_many
conn.close()