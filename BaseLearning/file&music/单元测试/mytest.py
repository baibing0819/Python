#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: mytest.py
@time: 6/27/19 4:28 PM
@desc:
'''

import unittest
from 单元测试_func import mySum
from 单元测试_func import mySub


class Test(unittest.TestCase):
    def setUp(self):
        print("开始测试是自动调用")

    def tearDown(self):
        print("结束测试时自动调用")

    #测试mySum
    def test_mySum(self):
        self.assertEqual(mySum(1,2),3,"加法有误")

    def test_mySub(self):
        self.assertEqual(mySub(2,1),1,"减法有误")


if __name__ == "__main__":
    unittest.main()



