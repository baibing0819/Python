#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: 9、线程通讯.py
@time: 7/5/19 10:00 AM
@desc:
'''

import  threading , time


def func():
    #事件对象
    event = threading.Event()
    def run():
        for i in range(5):
            #阻塞，等待事件的触发
            event.wait()
            event.clear()
            print("ice bai is a good man !!--%d"%i)
    t = threading.Thread(target=run).start()
    return event


e = func()


#触发事件:
for i in range(5):
    time.sleep(2)
    e.set()