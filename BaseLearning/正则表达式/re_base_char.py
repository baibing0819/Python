#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: re_base_char.py
@time: 6/28/19 1:56 PM
@desc:
'''

import re

print("---------------匹配单个字符与数字---------------")
'''
.   匹配除换行符意外人任意字符
[0123456789]    []是字符集合，表示匹配括号内所包含的任意一个字符
[icebai]        匹配 'i' 'c' 'e' 'b' 'a' 'i' 中任意一个字符
[a-z]、[A-Z]           匹配任意小/大写字符
[0-9]           匹配任意数字
[0-9a-zA-Z]     匹配任意数字和字母
[0-9a-zA-Z_]     匹配任意数字和字母、下划线
[^icebai]       匹配除了 icebai这几个字符意外的所有字符，^称为脱字符，表示不匹配集合中的字符
[^0-9]          匹配所有的非数字字符
\d              匹配数字，效果同[0-9]
\D              匹配非数字字符
\w              匹配数字、字母和下划线
\s              匹配任意的空白符(空格、换行、回车、换页、置表) ，效果同  [ \f\n\r\t]
\S              匹配任意的非空白符 效果同  [^ \f\n\r\t]

'''

print(re.search(".","icebai is a good man "))
print(re.search("[0213456789]","icebai is a good man 5"))

print("----------------锚字符（边界字符)------------------")
'''
^           行首匹配，和在[^]里的 ^ 不是一个意思 
$           行尾匹配
\A          匹配字符串开始， 它和 ^ 的区别是：\A 只匹配整个字符串的开头，即使在  re.M模式下也不会匹配其他行的行首
\Z          匹配字符串结束，它和 $ 的区别 ：\Z 只匹配整个字符串的结尾，即使在  re.M模式下也不会匹配其他行的行尾
\b          匹配一个单词的边界，也就是值单词和空格见的位置 
            
\B          匹配非单词边界


'''

print(re.search("man$","ice bai is a good man"))

print(re.search(r"er\b","never give up"))
print(re.search(r"er\b","never"))
print(re.search(r"er\b","nerve"))

print("-----------------匹配多个字符---------------------")
'''
说明：下方的 x y z 均为假设的普通字符，n m为非负整数 ，不是正则表达式的元字符

(xyz)       匹配小括号内的xyz(作为一个整体去匹配)
x？         匹配0个或者1个x
x*          匹配0个或者任意多个x
.*          匹配0个或任意多个字符(换行符除外)
x+          匹配至少一个x
x{n}        匹配确定的n个x,n是一个非负整数
x{n,}       匹配至少n个x
x{n,m}      匹配至少n个最多m个x   n <= m
x|y         | 表示或，匹配的是x或y


'''

print(re.findall(r"a?","aaa"))
print(re.findall(r"a*","aaabaaa"))  #贪婪匹配，匹配尽量多的字符，所以结果只有aaa和空
print(re.findall(r"a+","aaabaaa"))
print(re.findall(r"((s|S)un)","sun -- -- Sun -- sfd --- Sdd"))


print("-----------------------特殊--------------------")
'''
*?    +?   (xyz)?   最小匹配,通常正则表达式是尽可能多的匹配，可以使用这种解决贪婪匹配 
(?:x)               类似(xyz),但它不表示一个组

'''

str = "bai is a good man !   bai is a nice man !  bai is a handsome man !!!"
print(re.findall(r"bai.*?man",str))