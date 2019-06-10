'''Sets'''
''' In sets no duplacates value in below example 
a = {1, 2, 3, 1}
the outout will be 
([1, 2, 3])

Note: Sets are not indexed or ordered
It will throw TypeError: 'set' object does not support indexing
'''
a = {1, 2, 3, 1}
print(a)

print('Length of A', len(a))

'''Add element to set
if that element is already in set then nothing will happen'''
a.add(10)
print(a)
a.add(10)
print('Again added same value:', a)

a.update([15, 18, 19, 20])
print(a)

a.remove(15)
print(a)

a.discard(20)
print(a)

'''The diffrence between discard and remove is :
If thete element is not persern in set them remove will throw KeyError 
but in discard it won't throw any error.'''

a.pop()
print(a)
a.clear()
print(a)

print(type(a))
del a
print('del will delete the set')

'''create set usint constructor'''
name = set(['max', 'alena', 'moonstone'])
print(name)

z = set([1, 2, 3, 4, 5, 6])
print(type(name))
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



print(dir(z))