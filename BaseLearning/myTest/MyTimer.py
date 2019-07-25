#对象相关的练习

import time as t
tim_stu = ['年','月','日','时','分','秒']

class MyTimer():

    def __init__(self):
        self.lasted = []
        self.begin = 0
        self.end = 0
        self.prompt = '未开始计时'

    def __str__(self):
         return self.prompt

    __repr__ = __str__

    #计时开始函数
    def start(self):
        self.prompt = '请先停止计时器再开始计时'
        self.begin = t.localtime()
        print('开始计时...')

    #计时结束函数
    def stop(self):
        if not self.begin:
            print('请先开始计时...')
        else:
            self.end = t.localtime()
            self.cal_lasted()
            print('结束计时...')

    #定义两个计时器运行时间相加的方法
    def __add__(self,other):
        self.prompt = '共运行时间为 '
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                self.prompt += str(result[index]) + str(tim_stu[index])

        return self.prompt

    #计算时间戳
    def cal_lasted(self):
        self.prompt = '此次运行时间为 '
        for index in range(5,-1,-1):
            #调整时间表示，防止负数的出现(视为两个数相减的操作)  
            index_temp = index                          #index_temp 用于调整
            temp = self.end[index] - self.begin[index]
            if temp < 0 :
                index_temp -= 1
                while index_temp > 2:                    #目前只检测时分秒
                    if self.end[index_temp] > 0:         #检查高位是否够借
                    self.end[index_temp] -= 1            ###### 这里依旧存在bug  'time.struct_time' object does not support item assignment
                        self.lasted.append(self.end[index] - self.begin[index] + 60)
                        break;
                    else:
                        index_temp -= 1
            else:
                self.lasted.append(self.end[index] - self.begin[index])

        for i in range(5,-1,-1):
            if self.lasted[i]:
                self.prompt += str(self.lasted[i]) + str(tim_stu[5-i])


        self.begin = 0
        self.end = 0    #结束后重新初始化
        
