#问题描述：人开枪射击子弹
#@Time  : 2019/6/18 下午2:18
#@Author: baibing
#@File  : mainFunc.py

'''
对象分析：
对象：人
    属性：枪
    行为：开火、填充子弹

对象：枪
    属性：弹夹
    行为：射击

对象：弹夹
    属性：子弹数量
    行为

'''

from person import Person
from clip import Clip
from gun import Gun

clip = Clip(5)
gun = Gun(clip)
person = Person(gun)

person.fire()
person.fire()
person.fire()
person.fire()
person.fire()
person.fire()

person.fillBullet(2)
person.fire()
person.fire()
person.fire()
