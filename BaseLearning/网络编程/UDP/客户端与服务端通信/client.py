#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: client.py
@time: 7/3/19 3:32 PM
@desc:
'''

import socket

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    data = input("请输入数据：")              #发送数据
    client.sendto(data.encode("utf-8"),("172.20.124.131",8092))
    info = client.recv(1024).decode("utf-8")
    print("服务器说：",info)