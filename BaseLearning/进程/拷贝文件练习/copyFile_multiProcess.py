#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: copyFile_multiProcess.py
@time: 7/3/19 7:30 PM
@desc:
'''

from multiprocessing import Pool
import os, time, random

#实现文件的拷贝
def copyFile(rPath,wPath):
    fr = open(rPath,"rb")
    fw = open(wPath,"wb")

    context = fr.read()
    fw.write(context)
    fr.close()
    fw.close()


path = r"/home/baibing/prj/pycharmPrj/test/进程/拷贝文件练习/file"
topath = r"/home/baibing/prj/pycharmPrj/test/进程/拷贝文件练习/toFile"

if __name__=="__main__":
    # 读取path下面所有的文件
    fileList = os.listdir(path)

    start = time.time()
    pool = Pool()
    for fileName in fileList:
        pool.apply_async(copyFile,args=(os.path.join(path,fileName),os.path.join(topath,fileName)))

    pool.close()
    pool.join()

    end = time.time()
    print("复制完毕，耗时 %0.8f" % (end - start))



