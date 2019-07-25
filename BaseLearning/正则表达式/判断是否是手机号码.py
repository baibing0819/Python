#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: 判断是否是手机号码.py
@time: 6/28/19 10:32 AM
@desc: 给你一串字符串，判断是否是电话号码
'''

import re

def checkPhone(str):
    if len(str) != 11:
        return False
    elif str[0] != "1":
        return False
    elif str[1:3] != "30" and str[1:3] != "39":
        return False
    for i in range(3,11):
        if str[i] < "0" or str[i] > "9":
            return False

    return True

def checkPhone2(str):
    pat = r"1(([3578]\d)|(47))\d{8}$"
    res = re.match(pat,str)
    print(res)
    return res


print(checkPhone("13929764831"))
print(checkPhone("1392s764831"))
print(checkPhone("139297648312"))
print(checkPhone("13929764831s"))
print(checkPhone("23929764831"))

print(checkPhone2("13929764831"))
print(checkPhone2("1392s764831"))
print(checkPhone2("139297648312"))
print(checkPhone2("13929764831s"))
print(checkPhone2("23929764831"))


'''0
QQ      6 - 10位数字
mail    sunddasd@163.com
phone   010-55327892
user
passwd
ip
url
'''

re_QQ   = re.compile(r"^[1-9]\d{5,9}$")
print(re_QQ.search("243061887"))
print(re_QQ.search("2430a61887"))
print(re_QQ.search("243061887121"))