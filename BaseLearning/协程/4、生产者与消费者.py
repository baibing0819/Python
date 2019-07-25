#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: 4、生产者与消费者.py
@time: 7/8/19 4:54 PM
@desc:
'''

'''
待理解
'''

def productor(c):
    c.send(None)
    for i in range(5):
        print("生产者产生数据%d"%i)
        r = c.send(str(i))
        print("消费者消费了数据%s"%r)
    c.close()



def customer():
    data = ""
    while True:
        n = yield data
        if not n:
            return
        print("消费者消费了%s"%n)
        data = "200"


c = customer()  #返回一个生成器
productor(c)    #将生成器传入，在生产者函数中运行从而触发消费者执行