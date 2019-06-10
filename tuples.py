'''Tuples are inmuttable means we can not change any content of tuple'''
t = (1, 1,2,3)
print(type(t))

print(t.count(1))

'''
IndexError: tuple index out of range 
print(t[100])
'''

'''
TypeError : 'tuple object does not support item assignnment
t[0]=2
'''
print('length of tuple t is', len(t))

'We can assigne multiple datatype in tuple' 
x = (1, 'Neelesh', 1.200)
print(x)

'''Concatnation of tuple'''
z = x + t
print(z)

a = ('hi') * 5
print(a)
a = ('Hello', ) * 3
print(a)

print(z)
print('Get max from the tuple:', max(z))
print('Get min from the tuple:', min(z))

x = (1, 3, 43, 2, 55, 46)
print('Get max from the tuple:', max(x))
print('Get min from the tuple:', min(x))

print('Delete the tuple "del x"')
del x
