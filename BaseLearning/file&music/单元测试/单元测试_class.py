#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: 单元测试_class.py
@time: 6/27/19 4:38 PM
@desc:
'''

class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getAge(self):
        return self.age