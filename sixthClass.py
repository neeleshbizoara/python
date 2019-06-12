#if we want to remove duplicate value we can use Set
list1 = [1,2,3,4,1,2,3]
x = set(list1)
print(x)

'''union'''
z = set([1, 2, 3, 4, 5, 6])
print(z)
print(type(z))

y = set([2, 4, 7, 9, 10, 13]) 

print('Union of 2 sets', z | y)
'''Another way to union'''
print(y)
print(z)
print(y.union(z))


'''Interscetion of 2 sets'''
print('Interscetion of 2 sets', z & y)
print('Interscetion of 2 sets', z.intersection(y))

'''Find out the diffrence between two sets'''
print('list all elements which are in z but not in y', z-y)
print('list all elements which are in y but not in z', y-z)
print('list all elements which are in z but not in y using diffreance() ', z.difference(y))
print('symmetric difference of 2 sets', z ^ y)
print('symmetric difference of 2 sets using symmetric_difference()', y.symmetric_difference(z))


str ="kaksdkjakssdjassdkivnfj"
set1 = set()
for x in str:
    if x not in 'abc':
        set1.add(x)
print(set1)


'''Dictionary'''
d = {'name': 'Neelesh', 15: 3*5, 15.01: 10.001, True: True}
dict1 = d.items()
print(dict1)
print(dict(dict1))

#dict comprehensions
#list comprehensions
q1 = [1,2,3]
q2 = ['name', 'xyz', 'asd']
dict1 = {x:y for x,y in zip(q1, q2)}

print(hash((1,2,3)))
print((1,2,3) == (1,2,3))
print([1,2,3] == [1,2,3])
print([1,2,3] is [1,2,3])

a = 1 #primitive data type
b = 1 #primitive data type always be in memory until execution is going on 
print(a is b)

p = 1
abc = p
efg = abc
del p
print(abc)
del abc
print(efg)
del efg
# print(abc)
# print(efg)

print(dict1)



l1 = ['a','b','c','d','e']
for x in enumerate(l1):
    print(x)

'''
return type of sorted() and reversed()
'''