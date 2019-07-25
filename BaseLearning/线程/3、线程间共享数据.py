#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: 3、线程间共享数据.py
@time: 7/3/19 11:11 PM
@desc:
'''
import threading

'''
多线程和多进程最大的不同在于：多进程的同一个变量各自有一个备份存在与各个子进程中，互不影响;而多线程中，变量由所有线程共享，所以任何一个
变量都可以被任意一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时修改一个变量，容易把内容该乱了。

'''

num = 100

def run(n):
    global num
    for i in range(1000000):
        num = num+n
        num = num-n

if __name__=="__main__":
    t1 = threading.Thread(target=run,args=(6,))
    t2 = threading.Thread(target=run,args=(9,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("num = %d" % num)

