#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: 6、信号量控制线程数量.py
@time: 7/4/19 4:59 PM
@desc:
'''

import threading
import time

sem = threading.Semaphore(2)   #虽然有5个线程，但信号量可以控制运行数量

def run():
    with sem:
        for i in range(10):
            print("%s -- %d"%(threading.current_thread().name,i))
            time.sleep(1)


if __name__=="__main__":
    for i in range(5):
        threading.Thread(target=run).start()