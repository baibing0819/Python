#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: 进程间通信.py
@time: 7/3/19 10:35 PM
@desc:
'''

from multiprocessing import Process ,Queue
import  os,time


def write(q):
    print("启动写子进程%s"%(os.getpid()))
    for chr in ["A","B","C","D"]:
        q.put(chr)
        time.sleep(1)
    print("结束写子进程%s" % (os.getpid()))

def read(q):
    print("启动读子进程%s"%(os.getpid()))
    while True:
        value = q.get(True)
        print("value = " + value)
    print("结束读子进程%s"%(os.getpid()))

#>>>>>>>>>>>>>>>>>>>利用队列进行通信<<<<<<<<<<<<<<<<
if __name__=="__main__":

    print("主(父)进程启动...")

    #父进程创建队列，并传递给子进程(引用)
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))

    pw.start()
    pr.start()

    pw.join()
    pr.terminate()  #pr进程里是死循环，无法等待其结束，只能强行结束

    print("父进程结束...")

    # while True:
    #     pass
