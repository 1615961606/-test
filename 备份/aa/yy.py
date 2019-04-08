class Car():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return '你好你拨打的电话已关机，请扫后再拨%s%s'%(self.name,self.age)
print('大家好')
msld = Car('肥肥',8)
print(msld)