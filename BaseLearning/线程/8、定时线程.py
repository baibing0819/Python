#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: 10、定时线程.py
@time: 7/5/19 9:57 AM
@desc:
'''

import  threading

def run():
    print("ice bai is a good man")

#延时执行线程
t = threading.Timer(5,run)
t.start()

t.join()
print("父进程结束")