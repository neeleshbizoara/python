print("Helllo");

list = [1,2,3]
print(list)
print(type(list))

'''
list name can not be list 'not good practice'
'''

'''
Assignment 
remove all repeted value from list
'''

print('one' > 'onf')
print('one' > 'one')
print('one' > 'five')

'''
pop can also take index
example list.pop(0) // it will remove first indexed value
But its not recmended
So we can use collection cover in 5.1.2. Using Lists as Queues
'''

'''
Assignment 
multipy 2 list
[x*w for x,w in zip(y,z)]
'''


#tuple
tup = (5)
print(tup)
print(type(tup))
tup = 5,
print(tup)
print(type(tup))
tup = (1,2,3,"TEst")
print(len(tup))
x,y,z,t = tup
print('x: {0}, y: {1}')
tup = ([1,2,3], [4,5,6])
del tup[0][0]
print(tup)

tt = (1,2,3,4)
print(hash(tt))
print(id(tt))
del tt

a="Hello"
b="Hello"
print(id(a))
print(id(b))
print(hash(a))
print(hash(b))

print(a is b)
print(a == b)
a = [1,2,3]
b=[1,2,3]
print(id(a))
print(id(b))
#print(hash(a)) //Throw Error "TypeError: unhashable type: 'list"
#print(hash(b)) //Throw Error "TypeError: unhashable type: 'list"


tup1 = (1,2,3)
tup2 = (1,2,3)
print(id(tup1))
print(id(tup2))
print(hash(tup1))
print(hash(tup2))

#test # Throw Error NameErro: name 'test' is not defined


'''di = {1: "One", 2:"Two", 3: "three"}
l = {**di}
print(l)'''

'''q = lambda x, y: x + y
print(q(10,20))

def CTOF(x = int(input())):
    return (x* 9/5)+32

print(CTOF())'''

inp = int(input())
for x in range(inp):
    print(x*x)

def fun1():
    pass
    print('10')

fun1()