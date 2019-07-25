#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: server.py
@time: 7/4/19 11:19 AM
@desc: 通过客户端和服务器端同一ip下的连接(即连接同一个服务器)，然后不同客户端之间相互发送信息实现聊天的功能，客户端的消息会先发到服务器，服务器作为
        中转站将消息转发给要发送的另一个客户端，从而实现聊天功能。
'''

import tkinter
import socket
import threading

win = tkinter.Tk()
win.title("chatroom-Server")
win.geometry("400x400+200+20")

users = {}

#新建一个线程用于启动服务器，并让他执行接收客户端的消息
def startServer():
    #新建一个服务器启动的线程
    t_server = threading.Thread(target=start)
    t_server.start()

#服务器端(线程)执行的功能函数，接收客户端消息
def start():
    ipStr = eIp.get()
    portStr = ePort.get()       #获得登陆时输入的ip、port

    #创建server端固定步骤
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket

    server.bind((ipStr, int(portStr)))  # 绑定ip端口

    server.listen(10)  # 监听 ,参数为监听数量，允许几个连接服务器

    printStr = "服务器启动成功..."
    text.insert(tkinter.END, printStr)


    # 等待接收来自客户端的消息
    while True:
        clientSocket, clientAddress = server.accept()  # 等待连接,可以获得客户端socket号和地址
        print("%s -----  %s  连接成功" % (str(clientSocket), clientAddress))

        #新建线程，执行函数功能：让服务器端一直等待接收客户端的消息，并转发给他想发送的另一端
        t = threading.Thread(target=run, args=(clientSocket,clientAddress))
        t.start()

def run(ck,ca):
    print("*******************")

    userName = ck.recv(1024)            #接收客户端发来的登陆用户信息
    users[userName.decode("utf-8")] = ck #将客户端的socket号(连接时获取到的)和用户名保存到用户字典里
    print(users)
    # printStr = userName + "连接"
    # text.insert(tkinter.END,printStr)

    while True:
        rData = ck.recv(1024)   #接收用户端发来的信息
        dataStr = rData.decode("utf-8")

        msgList = dataStr.split("|_")    #按约定的格式获取到想要发送给对方的用户名，以便下一句转发用户信息到该用户
        # 转发信息，即用该用户名字对应的socket号发送信息
        users[msgList[0]].send(msgList[1].encode("utf-8"))

#>>>>>>>>>>>>>>>>>>>>界面设计<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
labelIP = tkinter.Label(win,text="ip",font=("黑体",20)).grid(row=0,column=0)
labelPort = tkinter.Label(win,text="port",font=("黑体",20)).grid(row=1,column=0)

eIp = tkinter.Variable()
ePort = tkinter.Variable()
entryIp = tkinter.Entry(win,textvariable=eIp).grid(row=0,column=1)
entryPort = tkinter.Entry(win,textvariable=ePort).grid(row=1,column=1)

button = tkinter.Button(win,text="启动",command=startServer).grid(row=2,column=0)

text = tkinter.Text(win,width=30,height=10)
text.grid(row=3,column=0)


win.mainloop()