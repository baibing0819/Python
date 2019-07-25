#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: 封装进程对象.py
@time: 7/3/19 7:48 PM
@desc:
'''

from myProcessObj import myProcess

if __name__=="__main__":
    print("父进程启动")

    p = myProcess("test")

    p.start()
    p.join()

    print("父进程结束")