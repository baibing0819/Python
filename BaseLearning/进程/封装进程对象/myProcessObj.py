#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: myProcessObj.py
@time: 7/3/19 7:46 PM
@desc:
'''

from multiprocessing import Process
import  os,time

class myProcess(Process):
    def __init__(self,name):
        Process.__init__(self)
        self.name = name

    def run(self):
        print("子进程(%s-%s)启动" % (self.name,os.getpid()))
        time.sleep(3)
        print("子进程(%s-%s)结束" % (self.name, os.getpid()))
