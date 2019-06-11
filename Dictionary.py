'''Dictionary'''
'''A dictionary is a collection which is unordered, changeable and indexed. 
In Python dictionaries are written with curly brackets, and they have keys and values.'''

d = {
    "Member": {
        'firstName': 'Neelesh',
        'lastName': 'Bizoara',
        'age': 32,
        'gender': 'Male',
        'isMarried': True,
        'working': True,
    }
}

''',
    "Member": {
        'firstName': 'Reun',
        'lastName': 'Bizoara',
        'age': 28,
        'gender': 'Female',
        'isMarried': True,
        'working': True,
    }'''

print(type(d))
print(d)

print(d['Member'])
print(d['Member']['firstName'])
print(len(d))
print(len(d["Member"]))

d.clear()
print('Clear function will clear the dictionary', d)

print('to delete Dictionary we can use del')
del d
'''print(d) #As d is deleted and we are trying to acced d it will throw NameError: name 'd' is not defined'''

# we can use string, int, float, and boolean as key in dictionary
d = {'name': 'Neelesh', 15: 3*5, 15.01: 10.001, True: True}
print(d)
print(d[True])
print(d[15])

'''What happen when key is not in dictionary and we try to get value of that
print(d[100]) # It will throw KeyError 
'''

#We can also use tuple as key 
# We can use any type as value for example string, int, float, boolean or collection as value
d = {(2,3): 5}
print(d)
val = d[(2,3)]
print(val)

d = {'name': 'Neelesh', 15: 3, 15.01: 10.001, True: True}
# we have get method to get val of a give key
val = d.get(15)
print(val)
val = d.get('name')
print(val)
val = d.get(15.01)
print(val)

# We can also add new key-value in dictionary 
d['lastName'] = 'Bizoara'
print(d)

#We can remove any key value pair from dictionary
d.pop('lastName')
print(d)

# We can also update the value of dictionary
d['name'] = 'Neelesh Bizoara'
print(d)

#Similarly update method will update value of the key
d.update({'name': 'Neelesh'})
print(d)


#Keys method will listout all the keys of dictionary
print(d.keys())
print(type(d.keys()))

#There is also a method which will list all the values
print(d.values())
print(type(d.values()))

#We can alsi list all the key value pair from the dictionary
print(d.items())
print(type(d.items()))
print(d.items()[0])
print(len(d.items()[0]))
print(d.items()[0][1])

#popitem method will remove the last key value pair from dictionary which we haved updated or added.
d = {'name': 'Neelesh', 'age': 32, 'lastname': 'Bizoara'}
print(d)
d.popitem()
print(d)
d['isMarried'] = True
print(d)
d.popitem()
print(d)