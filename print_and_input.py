x = 10
y = 20
print('{0} * {1} = {2}'.format(x, y, x*y))
print('Neelesh', 'Bizoara', sep="@@") #sep is a keyword of print method
print('Neelesh', 'Bizoara', sep='x*y')
print('Neelesh', 'Bizoara', sep=" ")
print('Neelesh', ' ', 'Bizoara')
print('Neelesh', 'Bizoara')


name = 'Python'
course = 'Course'
print('Hello %s' %name)
print('Welcome to %s Tutorial %s' %(name, course))

name = 'Neelesh'
age = 32
print('Hello %s ! are you %d years old.' % (name, age))
print("Marks = %f" % 92.5)
print("Marks = %.2f" % 92.5)

'''
#Input
value = input("Enter some value:")
if type(value) == int:
    print("%d is intiger number" %value)
else:
    print("{0} is string value".format(value))

#typecast string to intiger value
value = int(input("Enter some value:"))
if type(value) == int:
    print("%d is intiger number" %value)
else:
    print("{0} is string value".format(value))
    
#Built-in Functions and Built-in Module
# Some of them are print, input, int, float we seen all these
'''

# How we cam list all build in functions and type
print(dir(__builtins__))

x = 2**10 #it give 2 to power of 10
print(x)
x = pow(3, 10)
print(x)
length_str = len("this method return length  of the string")
print(length_str)
help(max)
print("Get the Max number {0}".format(max(1, 2, 3,4, 44, 12,1,234,2)))

import math
print('Square root of 100 is :',math.sqrt(100))

print('Built in method\'s of math module\n', dir(math))
print("Built in Modules in python\n", help('modules'))

import formatter
print(dir(formatter))
#print(help(formatter.warnings))
input("Press any key to exit")

import datetime
#print(dir(datetime))
currentTime = datetime.datetime.now()
print(currentTime.strftime("%A %d %Y"))

#Python string
x = '     Hello'
y = 'hello'
z = 'HELLO'
p = 'Hello, World'

print(y.capitalize())
print(y.upper())
print(z.lower())
print(y[0])
print(y[0:2]) #Substring
print(x)
print(x.strip())
print(z, 'is lower', z.islower(), ',', y, 'is lower', y.islower())
print(z, z.isupper(), sep = ' is upper ')
print(y, y.isupper(), sep = ' is upper ')
print(x.replace(' ', '@'))
print(p.split(','))
# print(y+10) throw TypeError: can only concatenate str  (not "int") to str
print(y*10)
print(x.find('h'))

