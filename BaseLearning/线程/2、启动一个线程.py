#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: 2、启动一个线程.py
@time: 7/3/19 11:00 PM
@desc:
'''

import threading
import time

def run():
    print("子线程(%s)启动..." % (threading.current_thread().name))

    #实现线程的功能
    time.sleep(2)
    print("this is a thread running....")
    time.sleep(2)


    print("子线程(%s)结束..." % (threading.current_thread().name))


if __name__=="__main__":
    #任何一个进程默认会启动一个线程。称为主线程，主线程可以启动子线程
    print("主线程(%s)启动..."%(threading.current_thread().name))   #返回当前线程实例的名称

    #创建子线程，name是子线程的名称
    t = threading.Thread(target=run,name="runThread")
    t.start()

    #等待子线程结束
    t.join()

    print("主线程(%s)结束..."%(threading.current_thread().name))   #返回当前线程实例的名称

