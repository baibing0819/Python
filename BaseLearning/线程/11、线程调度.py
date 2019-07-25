#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: 线程调度.py
@time: 7/8/19 3:57 PM
@desc:
'''

import threading
import time

#线程条件变量
cond = threading.Condition()

def run1():
    with cond:
        for i in range(0,10,2):
            print(threading.current_thread().name,i)
            time.sleep(1)
            cond.wait()
            cond.notify()

def run2():
    with cond:
        for i in range(1,10,2):
            print(threading.current_thread().name, i)
            time.sleep(1)
            cond.notify()
            cond.wait()

threading.Thread(target=run1).start()
threading.Thread(target=run2).start()