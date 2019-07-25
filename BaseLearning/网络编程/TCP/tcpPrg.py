#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: tcpPrg.py
@time: 7/3/19 11:27 AM
@desc: 客户端：创建TCP连接时，主动发起连接的叫做客户端
       服务端：接受客户端的连接

       1、启动服务器，准备接受客户端请求
       2、客户端发送请求
       3、握手
       4、传送数据
       5、结束
'''

import socket

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>客户端<<<<<<<<<<<<<<<<<<<<<<<<<<

#创建一个socket,参数：1、指定协议  AF_INET = IPV4   AF_INET6 = IPV6
#                    2、SOCK_STREAM 执行使用面向流的TCP协议
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#建立连接 ,参数是一个元组 第一个为要连接的服务器的ip地址，第二个参数为端口号
sk.connect(("www.sina.com.cn",80))

#客户端发送数据,b表示字节流，后面为固定格式
sk.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

#客户端等待接受数据
data = []
while True:
    tempData = sk.recv(1024) #每次接收1k的字节
    if tempData:
        data.append(tempData)
    else:
        break

dataStr = (b''.join(data)).decode("utf-8")   #将字节数据连成字符串

#客户端断开连接
sk.close()
# print(dataStr)

headers,HTML = dataStr.split('\r\n\r\n',1)
print(headers)
print(HTML)