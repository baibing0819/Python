#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: 冒充飞Q.py
@time: 7/3/19 3:18 PM
@desc:
'''

'''
TCP是建立可靠的连接，并且通信双方都可以以流的形式发送数据，相对于TCP，UDP则是面向无连接的协议

使用UDP协议时，不需建立连接，只需要知道对方的IP地址和端口号，就可以直接发送数据包，但是能不能到达就不知道了

虽然UDP传输数据不可靠，但他的优点和TCP相比，速度快，对于要求不高的三数据可以用UDP

'''

import socket
import time

#>>>>>>>>>>>>>>>>>>>>客户端<<<<<<<<<<<<<<<<<<<<<<<

udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)       #创建一个socket
udp.connect(("172.20.124.131",8091))                        #连接
udp.sendto("hello,ice bai man ".encode("utf-8"),("172.20.124.131",8091))
while True:
    # udp.send("ice bai is a good man ".encode("utf-8"))          #直接发送数据
    time.sleep(5)