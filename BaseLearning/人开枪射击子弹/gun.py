#问题描述： gun class
#@Time  : 2019/6/18 下午2:28
#@Author: baibing
#@File  : gun.py

class Gun(object) :
    def __init__(self,clip): #将弹夹类当做枪的属性传入
        self.clip = clip

    def shoot(self):
        if self.clip.bulletcount <= 0 :
            print('没有子弹了！ 请填充子弹')
        else:
            self.clip.bulletcount -= 1
            print("已射击，当前剩余子弹： %d" %(self.clip.bulletcount))