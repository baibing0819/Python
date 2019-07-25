#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: map&reduce.py
@time: 6/26/19 5:23 PM
@desc: 高阶函数 map reduce
'''
from functools import reduce

# Google 文章 提出 ， 大数据：hadoop spark storm Jstorm zookepeer kafka spring
#python 内置了map()和reduce()函数

#map()
#原型 map(fn,lsd)    fn:函数  lsd:列表   功能：将传入的函数依次作用在序列中的每一个元素，并把结果作为新的iterator返回

#将单个字符转换成对应的整数
def chr2int(chr):
    return {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,
            "8":8,"9":9,}[chr]

list1 = ["2","1","6","5"]

res = map(chr2int,list1)   #返回的是惰性列表
print(res)
print(list(res))


#[1,2,3,4] -> ["1","2","3","4"]
l = map(str,[1,2,3,4])
print(l)
print(list(l))


#reduce(fn,lsd)  功能：一个函数作用在序列上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素累计运算
#reduce(f,[a,b,c,d]) == f(f(f(a,b),c)d)


#求一个序列的和
list2 = [1,2,3,4,5]

def mySum(x,y):
    return x+y

r = reduce(mySum,list2)
print(r)

#结合使用,  功能：将字符串转换成对应字符
def str2int(str):
    def fc(x,y):
        return x*10 + y

    def fs(chr):
        return {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                "8": 8, "9": 9, }[chr]

    return reduce(fc,map(fs,list(str)))   #先调用map返回整数列表，再用reduce合成为一个整数


print(str2int("123456"))