#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: client.py
@time: 7/4/19 11:54 AM
@desc:
'''

import tkinter
import socket
import threading

ck = None

win = tkinter.Tk()
win.title("chatroom-Client")
win.geometry("400x400+200+20")

#获取由服务器转发过来的用话消息
def getServerMsg():
    while True:
        data = ck.recv(1024)
        text.insert(tkinter.INSERT,data.decode("utf-8"))
        text.insert(tkinter.INSERT, "\n")

#连接服务器函数
def connectServer():
    global ck

    #客户端连接服务器时发送自己的ip、port、用户名等信息
    ipStr = eIP.get()
    portStr = ePort.get()

    userStr = eUser.get()

    #连接服务器固定步骤
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ipStr, int(portStr)))
    client.send(userStr.encode("utf-8"))

    ck =client #用于在发送消息函数里使用，这里是局部变量，所以用一个全局变量保存
    #等待接收数据，创建一个线程让它一直等待接收消息
    t =threading.Thread(target=getServerMsg)
    t.start()


#发送信息函数
def sendMsg():
    friend = efriend.get()
    userStr = eUser.get()
    sendStr = esendMsg.get()        #获取要发送的用户名字、本地用户名、要发送的信息
    sendStr = friend + "|_" + userStr + " : " + sendStr

    ck.send(sendStr.encode("utf-8"))    #将信息发送到服务器，再让其转发到指定用户



#>>>>>>>>>>>>>>>>>>界面设计<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
labelUser = tkinter.Label(win,text="userName ",font=("黑体",20)).grid(row=0,column=0)
eUser = tkinter.Variable()
entryUser = tkinter.Entry(win,textvariable=eUser).grid(row=0,column=1)

labelIp = tkinter.Label(win,text="ip",font=("黑体",20)).grid(row=1,column=0)
eIP = tkinter.Variable()
entryIp = tkinter.Entry(win,textvariable=eIP).grid(row=1,column=1)

labelPort = tkinter.Label(win,text="port",font=("黑体",20)).grid(row=2,column=0)
ePort = tkinter.Variable()
entryPort = tkinter.Entry(win,textvariable=ePort).grid(row=2,column=1)

button1 = tkinter.Button(win,text="启动",command=connectServer).grid(row=3,column=0)

#用于显示对方发来的信息
text = tkinter.Text(win,width=30,height=10)
text.grid(row=4,column=0)

#用于输入想要发送的信息
esendMsg = tkinter.Variable()
entrySendMsg = tkinter.Entry(win,textvariable=esendMsg).grid(row=5,column=0)

#用于输入想要发送的用户名字
efriend = tkinter.Variable()
entryFriend = tkinter.Entry(win,textvariable=efriend).grid(row=5,column=1)

button2 = tkinter.Button(win,text="发送",command=sendMsg).grid(row=6,column=0)

win.mainloop()