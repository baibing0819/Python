#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: 2、协程原理.py
@time: 7/8/19 4:44 PM
@desc:
'''

'''

Python对协程的支持是通过generator实现的

'''

def run():
    print(1)
    yield 10
    print(2)
    yield 20
    print(3)
    yield 30

#协程的最简单风格，控制函数的阶段执行，节约线程或进程的切换时间
#返回值是一个生成器
m = run()
print(next(m))
print(next(m))
print(next(m))