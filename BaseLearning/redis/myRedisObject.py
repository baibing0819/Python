#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: myRedisObject.py
@time: 7/12/19 1:31 PM
@desc:
'''

import redis


class MyRedis():
    def __init__(self,passwd,host="localhost",port=6379):
        self.__redis = redis.StrictRedis(host=host,port=port,password=passwd)

    def set(self,key,value):
        self.__redis.set(key,value)

    def get(self,key):
        if self.__redis.exists(key):
            return self.__redis.get(key)
        else:
            return ""