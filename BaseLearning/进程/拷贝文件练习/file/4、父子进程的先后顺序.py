#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: 父子进程的先后顺序.py
@time: 7/3/19 4:49 PM
@desc:
'''

#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: 启动进程实现多人物.py
@time: 7/3/19 4:26 PM
@desc:
'''

'''
multiprocessing 库
跨平台版本的多进程模块，提供了一个process类来代表于i个进程

'''

from multiprocessing import Process
import os
from time import sleep

#子进程代码
def run(str):
    print("子进程启动...")
    sleep(3)
    print("子进程结束...")

if __name__ == "__main__":
    print("主(父)进程启动...")

    p = Process(target=run,args=("yoyoyo",))     #创建一个进程，在当前进程中创建一个子进程,target代表要执行的任务
                                            #args代表进程的参数，即函数的参数，是元组形式，只有一个时要加逗号
    p.start()       #启动进程

    p.join()        #使子进程结束再执行父进程

    print("父进程结束...")

'''
从结果来看，父进程的结束不能影响子进程的执行，但在编写程序时应当使子进程结束再执行父进程

'''