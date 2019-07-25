#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: 5、全局变量在多个进程中不能共享.py
@time: 7/3/19 4:59 PM
@desc:
'''

'''
 在子进程中修改全局变量对父进程没有影响
 在创建子进程时对全集变量做了一个备份，父进程与子进程中的num是两个完全不同的变量

'''

from multiprocessing import Process
import os
from time import sleep

num = 100

def run():
    global  num
    print("子进程启动...")
    num += 1
    print(num)
    print("子进程结束...")

if __name__=="__main__":
    print("父进程开始...")

    p = Process(target=run)
    p.start()
    p.join()

    print("父进程结束...   %d"%num)
