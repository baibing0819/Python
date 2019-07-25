#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: mySql.py
@time: 7/11/19 11:12 AM
@desc:
'''

import pymysql

class mySQL:
    def __init__(self,host,user,passwd,dbName):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.dbName = dbName

    def connect(self):
        self.db = pymysql.connect(self.host,self.user,self.passwd,self.dbName)
        self.cursor = self.db.cursor()

    def close(self):
        self.cursor.close()
        self.db.close()

    def get_one(self,sql):
        res = None
        try:
            self.connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
            self.close()
        except:
            print("查询失败")

        return res

    def get_all(self,sql):
        res = ()
        try:
            self.connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            self.close()
        except:
            print("查询失败")

        return res

    def insert(self,sql):
        return self.__edit(sql)

    def updata(self,sql):
        return self.__edit(sql)

    def delete(self,sql):
        return self.__edit(sql)

    def __edit(self,sql):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql)
            self.db.commit()
            self.close()
        except:
            print("操作提交失败")
            self.db.rollback()

        return count   #返回执行了多少行