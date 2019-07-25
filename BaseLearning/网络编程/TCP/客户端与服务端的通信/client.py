#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: client.py
@time: 7/3/19 2:00 PM
@desc:
'''

import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("172.20.124.131",8090))

while True:
    data = input("请输入给服务器发送的数据：")
    client.send(data.encode("utf-8"))
    info = client.recv(1024)
    print("服务器说：" , info.decode("utf-8"))