#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: playMusic.py
@time: 6/25/19 3:05 PM
@desc: 播放音乐测试
'''

import time
import pygame

filepath = r"/home/baibing/prj/pycharmPrj/test/file&music/刺猬.mp3"

pygame.init()
pygame.mixer.init()    #初始化,linux环境下会报错，暂时没解决
track = pygame.mixer.music.load(filepath)   #加载音乐
pygame.mixer.music.play()    #播放
time.sleep(5)      #播放5s
# pygame.mixer.music.pause()  #暂停播放
pygame.mixer.music.stop()