#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: 6、启动大量子进程.py
@time: 7/3/19 5:20 PM
@desc:
'''

from multiprocessing import Pool
import os, time, random


def run(name):
    print("子进程%d启动----%s"%(name,os.getpid()))
    start = time.time()
    time.sleep(random.choice([1,2,3]))
    end = time.time()
    print("子进程%d结束----%s ----- 耗时%.2f"%(name,os.getpid(),end-start))

if __name__ == "__main__":
    print("主(父)进程启动...")

    #创建多个进程----进程池
    pool = Pool()      #表示可以同时执行的进程数量,默认大小是cpu核心数

    for i in range(9):
        pool.apply_async(run,args=(i,)) #创建进程放入进程池统一管理,第一个参数为进程的工作，后面为工作函数的参数

    #在调用join之前必须先调用close，调用close之后不能再继续添加进程了

    pool.close()
    pool.join()     #进程池对象调用join，会等待所有的子进程结束完毕再执行父进程

    print("父进程结束...")