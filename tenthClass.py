'''Classes'''

class abc():
    order = 112
    def changeState(self):
        self.order = 40
    def append(self):
        pass

obj = abc()
type(obj) # "__main__" ?
print(obj.order)
obj.changeState() # here chageState is attribute of instance
print(obj.order)
a = list()

obj.append()
a.append(1)

'''---------------------'''
d = 10
print(id(d))
def fun(r):
    x = r
    print(id(x))
    z = 10

fun(d)
#print(z)

'''---------------------'''

#Evert this is object in python
print(list.__mro__) # it is alway return tuple

print(dir(abc)) # it is alway return list


def parentFun():
    t = 'test'
    def fun1():
        print(t)
        var1 = 12
    def fun2():
        fun1()
        print(var1)