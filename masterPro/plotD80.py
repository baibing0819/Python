#问题描述：
#@Time  : 2019/5/30 下午2:20
#@Author: baibing
#@File  : plotD80.py

import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk

#修改为自己的数据文件所在路径
data = np.loadtxt('/home/icebai/Downloads/D80-Na1.dat')
plt.title('D80-Na1 View')
plt.xlabel('x')
plt.ylabel('y')
fig = plt.Figure

data_x = data[:,0].tolist()
data_y = data[:,1].tolist()

new_data_x = []     #用于绘制数据均值的数据列表
new_data_y = []
countour_data_x = []    #用于绘制轮廓的数据列表
countour_data_y = []

#函数：处理原始数据得到数据均值曲线
def data_deal(x,y):
    count1 = 0
    sum1 = 0
    temp_x = []
    temp_y = []
    for i in range(0,len(y)-140):           #等间距计算平均值
        count1 += 1
        sum1 += y[i]
        if count1 == 59 :
            ave = sum1/60
            count1 = 0
            sum1 = 0
            for j in range(i-60,i):         #去掉波动较大点
                if (y[i] - ave)**2 < 1 :
                    temp_x.append(x[i])
                    temp_y.append(y[i])
    return temp_x,temp_y

#画边界函数
def draw_countour(x,y):
    # 变量初始化：
    sum_value1 = 0      #用于计算最大最小值及对应下标的临时中间变量
    sum_value2 = 0
    sum_index1 = 0
    sum_index2 = 0
    ave_max = 0         #用于计算最大最小值及对应下标的临时变量
    ave_min = 0
    ave_max_index = 0
    ave_min_index = 0
    temp_max1 = []      #用于保存轮廓最大最小值的列表---上半部分
    temp_min1 = []
    max1_index = []
    min1_index = []
    temp_max2 = []          #用于保存轮廓最大最小值的列表---下半部分
    temp_min2 = []
    max2_index = []
    min2_index = []
    maxl = []           #最大最小值列表(用于计算轮廓，等间距保存20个较大、较小值)
    minl = []

    new_y = []          #复制原始数据列表以便求取最大最小值

    for i in range(0,len(x)-140,140):       #先将步长为140的序列复制到新列表
        for k in y[i:i+140]:
            new_y.append(k)

        new_y.sort()                    #排序
        # print(new_y)
        for l in new_y[0:20]:           #保存其中的20个较大、较小值
            minl.append(l)
        for l in new_y[120:140]:
            maxl.append(l)

        for i in maxl :                 #计算当前步长所在子列表的最大、最小值
            sum_value1 += i
            sum_index1 += y.index(i)

        for i in minl :
            sum_value2 += i
            sum_index2 += y.index(i)

        ave_max = sum_value1 / 20
        ave_min = sum_value2 / 20
        ave_max_index = sum_index1 / 20
        ave_min_index = sum_index2 / 20

        sum_value1 = 0             #每次循环得到结果后清零相关变量，以便下次计算
        sum_value2 = 0
        sum_index1 = 0
        sum_index2 = 0
        maxl = []
        minl = []
        new_y = []

        # print('{}    {}'.format(ave_max,ave_max_index))
        # print('{}    {}'.format(ave_min,ave_min_index))
        # print('\n')

        if ave_max > 20 or ave_min > 20:         #上半区域轮廓数据
            temp_max1.append(ave_max)
            max1_index.append(ave_max_index)
            temp_min1.append(ave_min)
            min1_index.append(ave_min_index)

        else:
            temp_max2.append(ave_max)               #下半区域轮廓数据
            max2_index.append(ave_max_index)
            temp_min2.append(ave_min)
            min2_index.append(ave_min_index)

    #构造上半部分轮廓
    temp_min1 = list(reversed(temp_min1))
    min1_index = list(reversed(min1_index))
    temp_max1.extend(temp_min1)
    max1_index.extend(min1_index)
    temp_max1.append(temp_max1[0])
    max1_index.append(max1_index[0])

    # 构造下半部分轮廓
    temp_min2 = list(reversed(temp_min2))
    min2_index = list(reversed(min2_index))
    temp_max2.extend(temp_min2)
    max2_index.extend(min2_index)
    temp_max2.append(temp_max2[0])
    max2_index.append(max2_index[0])

    return temp_max1,max1_index,temp_max2,max2_index

on_hit = False
#display函数，用于GUI的display button触发事件
def display():
    global on_hit
    global fig
    if on_hit == False:
        on_hit = True

        countour_data_y1, countour_data_x1,countour_data_y2,countour_data_x2 = draw_countour(data_x, data_y)
        # plt.scatter(countour_data_x1, countour_data_y1, label='data countour', color='g')
        # plt.scatter(countour_data_x2, countour_data_y2, label='data countour', color='g')
        # plt.plot(countour_data_x1, countour_data_y1, label='data countour',color = 'g')
        # plt.plot(countour_data_x2, countour_data_y2, label='data countour', color='g')
        plt.fill(countour_data_x1, countour_data_y1,'#808080',alpha = 0.2)  #填充区域，alpha为透明度(0-1)
        plt.fill(countour_data_x2, countour_data_y2, '#808080', alpha=0.2)


        # deal data
        new_data_x, new_data_y = data_deal(data_x, data_y)
        # plt.scatter(new_data_x,new_data_y,label = 'deal data')
        plt.plot(new_data_x, new_data_y, label='deal data',color = 'r')

        plt.legend()            #用于显示标签
        fig = plt.gcf()         #用于保存图片，防止图片变为空白
        plt.show()

    else:
        on_hit = False


#quit button触发 函数
def quit():
    window.destroy()

#save button 触发函数
def save_img():
    global fig
    fig.savefig('/home/icebai/Downloads/plotD80.svg') #需修改为自己要保存的图片路径

#>>>>>>>>>>>>   GUI   <<<<<<<<<<<<<<#
window = tk.Tk()     #实例化object，建立窗口
window.title('Plot Window')
window.geometry('800x600')    #设置窗口大小

l = tk.Label(window,text='hi,Please select the graphic parameters:',font=('Arial', 12))
l.grid(row = 0,column = 0,rowspan = 2)   #放置标签

#combobox--linewidth
l1 = tk.Label(window,text='line width::',font=('Arial', 12),
              width=30, height=2)
l1.grid(row = 2,column = 0,rowspan = 2)   #放置标签

num = tk.StringVar()       #创建变量，用var来接收鼠标点击具体选项的内容
numChosen = ttk.Combobox(window,width = 12,textvariable = num)
numChosen['values'] = (1,2,3,4,5,6)
numChosen.current(0)        #设置默认值,显示第几个
numChosen.grid(row = 2,column = 1,rowspan = 2)

#combobox--linecolor
l2 = tk.Label(window,text='line color::',font=('Arial', 12),
              width=30, height=2)
l2.grid(row = 4,column = 0,rowspan = 2)   #放置标签

color = tk.StringVar()       #创建变量，用var来接收鼠标点击具体选项的内容
colorChosen = ttk.Combobox(window,width = 12,textvariable = color)
colorChosen['values'] = ('green','red','blue')
colorChosen.current(0)        #设置默认值,显示第几个
colorChosen.grid(row = 4,column = 1,rowspan = 2)

#combobox--countourcolor
l3 = tk.Label(window,text='countour color::',font=('Arial', 12),
              width=30, height=2)
l3.grid(row = 6,column = 0,rowspan = 2)   #放置标签

color1 = tk.StringVar()       #创建变量，用var来接收鼠标点击具体选项的内容
outlineColorChosen = ttk.Combobox(window,width = 22,height = 100,textvariable = color1)
outlineColorChosen['values'] = ('green','red','blue')
outlineColorChosen.current(0)        #设置默认值,显示第几个
outlineColorChosen.grid(row = 6,column = 1,rowspan = 2)

button1 = tk.Button(window,text = 'display',font=('Arial', 12), width=10, height=1,command = display)
button1.grid(row = 8,column = 1,rowspan = 2)

button2 = tk.Button(window,text = 'save as svg',font=('Arial', 12), width=10, height=1,command = save_img)
button2.grid(row = 8,column = 2,rowspan = 2)

button3 = tk.Button(window,text = 'exit',font=('Arial', 12), width=10, height=1,command = quit)
button3.grid(row = 10,column = 1,rowspan = 2)

window.mainloop()

