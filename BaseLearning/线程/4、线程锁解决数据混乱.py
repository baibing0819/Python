#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: 线程锁解决数据混乱.py
@time: 7/3/19 11:37 PM
@desc:
'''
import threading
'''
两个线程同时工作，一个存钱，一个取钱 ，可能导致数据异常

解决思路：加锁，保证了数据不发生混乱，阻止了并发执行，以单线程的方式执行，大大的降低了效率

    弊端：由于可以存在多个锁，不同线程持有不同的锁，并试图获取其他的锁，可能形成死锁，导致多个线程挂起，只能靠操作系统强制终止

'''
num = 100
#创建锁对象
lock = threading.Lock()

def run(n):
    global num
    for i in range(1000000):
        #加锁,try防止死锁发生
        lock.acquire()
        try:
            num = num+n
            num = num-n
        finally:
            #解锁
            lock.release(),     #一定要释放

        '''
        另一种写法：(自动上锁和解锁)
        
        with lock:
            num = num +n
            num = num -n
        '''

if __name__=="__main__":
    t1 = threading.Thread(target=run,args=(6,))
    t2 = threading.Thread(target=run,args=(9,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("num = %d" % num)
