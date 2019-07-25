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
win.title("chatroom-Client1")
win.geometry("400x400+200+20")

def getServerMsg():
    while True:
        data = ck.recv(1024)
        text.insert(tkinter.INSERT,data.decode("utf-8"))
        text.insert(tkinter.INSERT,"\n")

def connectServer():
    global ck

    #客户端连接服务器时发送自己的ip、port、用户名等信息
    ipStr = eIP.get()
    portStr = ePort.get()

    userStr = eUser.get()

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ipStr, int(portStr)))
    client.send(userStr.encode("utf-8"))

    ck =client
    #等待接收数据
    t =threading.Thread(target=getServerMsg)
    t.start()



def sendMsg():
    friend = efriend.get()
    userStr = eUser.get()
    sendStr = esendMsg.get()
    sendStr = friend + "|_" + userStr + " : " + sendStr

    ck.send(sendStr.encode("utf-8"))




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

text = tkinter.Text(win,width=30,height=10)
text.grid(row=4,column=0)

esendMsg = tkinter.Variable()
entrySendMsg = tkinter.Entry(win,textvariable=esendMsg).grid(row=5,column=0)

efriend = tkinter.Variable()
entryFriend = tkinter.Entry(win,textvariable=efriend).grid(row=5,column=1)

button2 = tkinter.Button(win,text="发送",command=sendMsg).grid(row=6,column=0)

win.mainloop()