#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: useMySql.py
@time: 7/11/19 11:23 AM
@desc:
'''

from mySql import mySQL

s = mySQL("localhost","root","bai950915","test")

res = s.get_all('select * from bankcard where money<300')
for row in res:
    print("%d--%d" % (row[0], row[1]))