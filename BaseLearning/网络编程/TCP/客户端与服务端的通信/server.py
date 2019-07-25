#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: server.py
@time: 7/3/19 2:00 PM
@desc:
'''


import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)       #创建socket

server.bind(('172.20.124.131',8090))    #绑定ip端口

server.listen(5)    #监听 ,参数为监听数量，允许几个连接服务器

print("服务器启动成功......")

clientSocket, clientAddress = server.accept()  # 等待连接,可以获得客户端socket号和地址

print("%s -----  %s  连接成功" % (str(clientSocket),clientAddress))
#等待接收
while True:
    data = clientSocket.recv(1024)
    print("收到数据：" + data.decode("utf-8"))
    sendData = input("请输入给客户端发送的内容：")
    clientSocket.send(sendData.encode("utf-8"))