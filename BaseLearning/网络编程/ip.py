#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: ip.py
@time: 7/10/19 9:55 AM
@desc:
'''


import ipaddress
a = ipaddress.IPv4Address('192.168.1.2')
b = ipaddress.IPv4Network('192.168.1.0/24')

