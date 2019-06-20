'''Classes'''

class abc():
    order = 112
    def changeState(self):
        self.order = 40
    def append(self):
        pass

print(type(abc))
print(id(abc))
obj = abc() # instantiation
dir(abc)
type(obj) # "__main__" ?
print(obj.order)
obj.changeState() # here chageState is attribute of instance
print(obj.order) #attribute references
dir(obj)
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
        # print(var1)


class MyClass:
    """A simple example class"""
    i = 12345

    def __init__(self, p, q):
        '''Constructor function'''
        self.var1 = p
        self.var2 = q

    def f(self):
        return 'hello world'

    obj1 = MyClass('This is my first string.', 7)
    obj2 = MyClass('This is my second string.', 7)