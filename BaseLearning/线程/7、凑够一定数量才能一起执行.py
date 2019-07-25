#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: 7、凑够一定数量才能一起执行.py
@time: 7/5/19 9:53 AM
@desc:
'''

import threading
import time

bar = threading.Barrier(4)

def run():
    print("%s -- start"%threading.current_thread().name)
    time.sleep(1)
    bar.wait()      #满足凑够四个线程再继续向下执行
    print("%s -- end" % threading.current_thread().name)


if __name__=="__main__":
    for i in range(5):
        threading.Thread(target=run).start()