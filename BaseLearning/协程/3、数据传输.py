#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: 3、数据传输.py
@time: 7/8/19 4:48 PM
@desc:
'''


def run():

    #空变量，存储的作用，data始终为空
    data = ""
    r = yield data      #返回data，是一个生成器

    print(1,r,data)

    r = yield  data

    print(2, r, data)

    r = yield data

    print(3, r, data)

    r = yield data

#协程的最简单风格，控制函数的阶段执行，节约线程或进程的切换时间
#返回值是一个生成器
m = run()
#启动m
print(m.send(None))
print(m.send("a"))
