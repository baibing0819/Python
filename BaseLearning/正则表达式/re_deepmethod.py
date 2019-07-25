#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: re_deepmethod.py
@time: 6/28/19 3:41 PM
@desc:
'''

import re

'''
字符串切割：
'''

str1 = "bai is a        good man"
print(str1.split(" "))
print(re.split(r" +",str1))

print("---------------------------------------")

'''
re.finditer(pattern,str,flags)
func: 与finall类似，扫描整个字符串，返回的是一个迭代器

'''
str3 = "bai is a good man !  bai is a nice man ! bai is a handsome man !"
it = re.finditer(r"(bai)",str3)

while(True):        #用迭代器处理每个数据，防止数据太大，内存空间不足
    try:
        l = next(it)
        print(l)
    except StopIteration as e:
        break


print("---------------------------------------")

'''
字符串的替换和修改
sub(pattern, rep1, string, count=0 ,flags = 0)
subn(pattern, rep1, string, count=0 ,flags = 0)

pattern:正则表达式
repl:指定的用来替换的字符串
string:目标字符串
count:最多替换次数

func：在目标字符串中，以正则表达式的规则匹配字符串，再把他们替换成指定的字符串。可以指定替换的次数。默认替换所有

区别：sub 返回一个被替换的字符串，后者返回一个元组，第一个元素为被替换的字符串，第二个元素表示被替换的次数

'''

strb = "bai is a good good man !"
print(re.sub(r"good","nice",strb))
print(re.sub(r"good","nice",strb,count=1))
print(type(re.sub(r"good","nice",strb)))

print(re.subn(r"good","nice",strb))
print(type(re.subn(r"good","nice",strb)))


print("----------------------------------")

'''
分组：
概念：除了简单的判断是否匹配之外，正则表达式还有提取子串的功能。用()表示的就是分组

'''

stra = "010-53247654"

m = re.match(r"(\d{3})-(\d{8})",stra)
print(m)
print(m.group(0))   #使用序号获取对应组的信息，group（0）代表原始字符串，与提取的结果无关，上面提取的只有两个组
print(m.group(1))
print(m.group(2))
print(m.groups())   #查看匹配的各组的情况

m = re.match(r"(?P<first>(\d{3})-(?P<last>\d{8}))",stra) #给组起名字的方式
print(m.group("first"))
print(m.group("last"))


print("-----------------------------------")
'''
编译：当我们使用正则表达式时，re模块会做两件事
1、编译正则表达式，如果正则表达式本身不合法，会报错
2、用编译后的正则表达式去匹配对象

'''

pat = r"1(([3578]\d)|(47))\d{8}$"
#未编译正则表达式时的匹配方式
print(re.match(pat,"13012348246"))
#将正则表达式编译成一个对象后的匹配方式,当然匹配的其他方法都可以用编译后的正则表达式对象直接调用
re_telephone = re.compile(pat)
print(re_telephone.match("13012348246"))