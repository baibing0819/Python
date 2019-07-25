#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: 进程.py
@time: 7/3/19 4:17 PM
@desc:
'''

'''
对于操作系统而言，一个任务就是一个进程

进程是系统中程序执行和资源分配的基本单位。每个进程都有自己的数据端、代码段、堆栈段

'''

#单任务现象：

from time import sleep

def run():
    while True:
        print("want run ....")
        sleep(1)

if __name__ == "__main__":
    while True:
        print("from ice bai greetting")
        sleep(1)

    run()       #无法执行到这里