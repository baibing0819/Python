#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: 3、更新文档.py
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
collection.update_one({"name":"pig"},{"$set":{"age":33}})
#updata_one   update_many




conn.close()