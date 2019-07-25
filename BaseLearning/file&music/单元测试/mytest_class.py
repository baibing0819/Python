#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: mytest_class.py
@time: 6/27/19 4:48 PM
@desc:
'''

import unittest
from 单元测试_class import Person

class Test(unittest.TestCase):
    def test_init(self):
        p = Person("kobe",43)
        self.assertEqual(p.name,"kobe","属性赋值有误")

    def test_getAge(self):
        p = Person("kobe", 43)
        self.assertEqual(p.getAge(),p.age,"getAge函数有误")

if __name__ == "__main__":
    unittest.main()