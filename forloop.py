'''
A for loop is used to iterate ove a sequence which can be a list, tuple, set or dictionary
'''

a = [0,1,2,3,4,5] #list
b = (0,1,2,3,4,5,6,9) #tuple
c = {0,1,2,3,4,5,6,8,9} #set
d ='0123456789' #string
e = { #dictionary
    "name": "Neelesh",
    "age": 20
}

# in operator : it will give True or False, if that value is present in collection or not 
print(0 in a)
print('1' in d)
print('123' in d)
print('9453' in d)
print(4,3,6 in a)
'''
for x in a:
    print(x)

for x in b:
    print(x)

for x in c:
    print(x)

for x in d:
    print(x)
'''
for x in e:
    print(x)

for x in e.keys():
    print('Key is', x, 'value is', e[x])

for x in e.values():
    print(x)

for x in e.items():
    print(x)

for key, value in e.items():
    print(key, ' ', value)

# We can also use range() for iteration, which return us value starting from 0 to end-1

for x in range(6):
    print(x)

for x in range(10,15):
    print(x)

for x in range(15, 25, 2): #range(start, end, step)
    print(x)
else:
    print('Finished') # We can use else statment with loops, it will executed when for loop is finished 