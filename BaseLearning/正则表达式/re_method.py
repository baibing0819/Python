#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: re_method.py
@time: 6/28/19 11:25 AM
@desc:
'''

import re

'''
re.match(pattern,string,flags)
func:尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配，成功的话，返回NONE
par: flag 标志位，要匹配的模式
re.I    忽略大小写
re.L    做本地户识别
re.M    多行匹配，影响 ^ and $
re.S    匹配包含换行符在内的所有字符
re.U    根据Unicode字符集解析字符，影响\w \W \b \B
re.X    是我们以更灵活的格式理解正则表达式

'''

print(re.match("www","www.baidu.com"))
print(re.match("www","www.baidu.com").span())   #得到匹配的下标位置
print(re.match("www","wwW.baidu.com",flags=re.I))   #得到匹配的下标位置


print("===================================")

'''
re.search(pattern,string,flags)
func: 扫描整个字符串，并返回第一个成功的匹配
'''

print(re.search("icebai","good man is icebai!]ef icebai is nice"))

print("===================================")

''' 
re.findall(pattern,string,flags)
func: 扫描整个字符串，并返回所有符合的结果列表
'''
print(re.findall("icebai","good man is icebai!]ef icebai is nice"))