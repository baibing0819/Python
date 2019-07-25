#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: changeBgPic.py
@time: 6/26/19 4:16 PM
@desc:修改桌面背景图片 #windows  win+r   regedit -> HKEY_CURRENT_USER -> COntrol Panel -> Desktop ->WallPaper
'''

import win32api
import win32con
import win32gui

def setWallPaper(path):
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,
                                    win32con.KEY_SET_VALUE)

    win32api.RegSetValueEx(reg_key,"其他属性值",0,win32con.REG_SZ,"6")
    pass

path = "add your png path"
setWallPaper(path)