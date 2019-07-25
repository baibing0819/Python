#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: 2、查询文档.py
@time: 7/11/19 5:54 PM
@desc:
'''

from pymongo import MongoClient
from bson.objectid import ObjectId      #用于id查询
import pymongo

#连接服务器
conn = MongoClient("localhost",27017)

#连接数据库
db = conn.mydb

#获取集合
collection = db.student

# #查询部分文档
# res = collection.find({"age":{"$gt":18}})
# for row in res:
#     print(row)
#
#查询所有文档
res = collection.find()
for row in res:
    print(row)
#最新推荐使用insert_one insert_many

#统计查询
# res1 = collection.find().count()
res1 = collection.count_documents({"age":{"$gt":18}})
print(res1)

#根据id查询
res = collection.find({"_id":ObjectId("5d26e65dfe70c7f308af4f65")})
print(res[0])

#排序
# res = collection.find().sort("age")
res = collection.find().sort("age",pymongo.DESCENDING)
for row in res:
    print(row)


#分页
print("****************************")
res = collection.find().skip(3).limit(2)
for row in res:
    print(row)

conn.close()