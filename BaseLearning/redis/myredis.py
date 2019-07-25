#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: redis.py
@time: 7/12/19 1:20 PM
@desc:
'''

import redis


r = redis.StrictRedis(host="localhost",port=6379,password="bai950915")  #连接



#方法一：根据数据类型的不同，调用相应的方法
#写
r.set("white","nice")
#读
print(r.get("white"))

#方法二 pipline
#可以缓冲多条命令，然后依次执行，减少服务器-客户端之间的TCP数据包
pipe = r.pipeline()
pipe.set("white2","nice")
pipe.set("white3","nice")
pipe.set("white4","nice")       #都暂时放入缓冲
pipe.execute()          #执行上面的命令，这样就只执行一次tcp请求