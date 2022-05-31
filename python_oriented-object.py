
#请练习定义一个动物类，并创建出两个实例dog, cat，打印实例，再比较两个实例是否相等。
class Animal(object):
    pass
dog = Animal()
cat = Animal()
print(dog)
print(cat)
print(dog==cat)

#请定义一个动物类，并创建出两个实例dog, cat，分别赋予不同的名字和年龄并打印出来。
dog.name = 'xiaobai'
dog.age = 5
cat.name = 'xiaohua'
cat.age = 4
print("它叫{},它{}岁了".format(dog.name,dog.age))
print("它叫{},它{}岁了".format(cat.name,cat.age))


#请定义一个动物类，抽象出名字、年龄两个属性，并实例化两个实例dog, cat。
class Animals(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
dog = Animals('xiaobai',9)
cat = Animals('xiaohua',8)
print(dog.name,dog.age)
print(cat.name,cat.age)

#请给 Animal类添加一个类属性 count，每创建一个实例，count 属性就加 1，这样就可以统计出一共创建了多少个 Animal的实例。
class Animals(object):
    count = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Animals.count += 1
dog = Animals('xiaobai',9)
print(Animals.count)
cat = Animals('xiaohua',8)
print(Animals.count)
print(dog.name,dog.age)
print(cat.name,cat.age)
print(cat.count)

#请把上节的 Animal类属性 count 改为 __c该ount，再试试能否从实例和类访问属性。
class Animals(object):
    __count = 0
    def __init__(self,name,age):
        Animals.__count = Animals.__count + 1
        self.name = name
        self.age = age
        print(Animals.__count)
P1 = Animals('cat',1)
p2 = Animals('dog',1)
print(Animals.__count)

#请给Animal类的__init__方法中添加name和age参数，并把age绑定到__age属性上，看看外部是否能访问到。
class Animal(object):
    def __init__(self, name,age):
        self.name = name
        self.__age = age
P1 = Animal('cat',1)
p2 = Animal('dog',1)
print(P1.__age)
