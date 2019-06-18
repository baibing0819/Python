#问题描述： person类
#@Time  : 2019/6/18 下午2:23
#@Author: baibing
#@File  : person.py

class Person(object) :
    def __init__(self,gun):   #将枪类当做person的属性传入
        self.gun = gun

    def fire(self):
        self.gun.shoot()

    def fillBullet(self,count):
        self.gun.clip.bulletcount = count
        print("已填充子弹，当前剩余子弹：%d" %(self.gun.clip.bulletcount))