#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: 1、协程.py
@time: 7/8/19 4:28 PM
@desc:
'''

'''

子程序/函数：在所有语言中都是层级调用，比如A调用B，在B哭执行过程用又可以调用C，C执行完毕返回，最后是A执行完毕。是通过栈实现的，一个
线程就是执行一个子程序，子程序调用总是一个入口，一次返回；调用的顺序总是明确的

协程概述：看上去也是子程序，但执行过程中，在子程序的内部可中断，然后转而执行其他子程序，不是函数调用，有点类似CPU中断

'''

'''
函数调用：

def C():
    print("C--start")

    print("C--end")


def B():
    print("B--start")
    C()
    print("B--end")


def A():
    print("A--start")
    B()
    print("A--end")

A()

'''

def A():
    print(1)
    print(2)
    print(3)

def B():
    print("x")
    print("y")
    print("z")

'''
实现打印 1 2 x y z 3 ，且不用函数调用。看起来像是线程，但是用协程做。特点是一个线程执行

与线程相比，协程的执行效率极高，因为只有一个线程，也不存在同时写变量的冲突，在协程中共享资源不加锁，只需要判断状态
'''