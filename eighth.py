'''import os
os.getcwd()

#builid finction
list1 = [1,2,3]
#print(list1.__mro__())


while True:
    try:
        x= input('Enter any thing:')
        print(int(x))
    except: 
        pass
        print('Error found')
        exit()
        #break
        #raise
    else:
        print('Else block')
#ValueError:     # expression as identifier:
'''

print(NameError.__mro__)


class listClass(list):
    pass

obj1 = listClass()
print(obj1)
obj1.append(1)
print(obj1)

print(listClass.__mro__)

'''finally'''


'''Throw away variable  is _'''

x = [int(input())*2 for _ in range(4)]
print(x)