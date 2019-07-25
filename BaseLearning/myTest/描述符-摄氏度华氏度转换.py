#描述符练习
''' 描述符是将某种特殊类型的类的实例指派给另一个类的属性、
    其中特殊类包括 __get__(self,instance,owner)、
    __set__(self,instance,value)、__delete__(self,instance)'''

#建立摄氏度描述符类
class Celsius:
    def __init__(self,value = 26.0):
        self.degree = float(value)

    def __get__(self,instance,owner):
        return self.degree

    def __set(self,instance,value):
        self.degree = float(value)

#建立华氏度描述符类
class Fahrenheit:
    def __get__(self,instance,owner):
        return float(instance.cel*1.8+32)

    def __set__(self,instance,value):
        instance.cel = float((value - 32)/1.8)

#建立转换类
class DegreeSwitch:
    cel = Celsius() #将描述符类赋予给DegreeSwitch类的属性
    fah = Fahrenheit()

    #这样，就可以通过改变DegreeSwitch的实例化对象属性值，来
    #直接改变描述符类中的属性值
