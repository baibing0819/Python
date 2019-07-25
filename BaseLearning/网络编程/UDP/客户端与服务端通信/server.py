#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: server.py
@time: 7/3/19 3:32 PM
@desc:
'''

import  socket

udpServer = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

udpServer.bind(("172.20.124.131",8092))

while True:
    data , addr = udpServer.recvfrom(1024)      #接受来自客户端的数据，用recfrom
    print("客户端说：",data.decode("utf-8"))
    # info = input("请输入数据：")                  #服务端发送数据
    udpServer.sendto("....".encode("utf-8"),addr)