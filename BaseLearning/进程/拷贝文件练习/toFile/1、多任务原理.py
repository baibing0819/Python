#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: 多任务原理.py
@time: 7/3/19 3:58 PM
@desc:
'''

'''
单核CPU实现多任务原理：操作系统轮流让各个任务交替执行，CPU调度执行速度非常快，使人们感觉是同时运行的

多核CPU实现多任务原理：真正的多任务执行，当任务数量远远超出cpu数量时，依旧会轮流调度到各个核心上执行

并发：看上去一起执行，任务数多余cpu核心数
并行：真正的一起执行，任务数小于cpu核心数

实现多任务的方式：
1、多进程：
2、多线程：
3、协程：
4、多进程+多线程：

'''