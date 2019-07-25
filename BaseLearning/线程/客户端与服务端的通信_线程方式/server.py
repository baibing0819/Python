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
import threading

def run(ck):
    data = ck.recv(1024)
    print("收到数据：" + data.decode("utf-8"))
    # sendData = input("请输入给客户端发送的内容：")
    clientSocket.send("rec your info ...".encode("utf-8"))

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)       #创建socket

server.bind(('172.20.123.225',8091))    #绑定ip端口

server.listen(5)    #监听 ,参数为监听数量，允许几个连接服务器

print("服务器启动成功,等待客户端连接......")


#等待接收
while True:
    clientSocket, clientAddress = server.accept()  # 等待连接,可以获得客户端socket号和地址
    print("%s -----  %s  连接成功" % (str(clientSocket), clientAddress))

    t = threading.Thread(target=run,args=(clientSocket,))
    t.start()
