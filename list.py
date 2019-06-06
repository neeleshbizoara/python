x = [1, 2, 3, 4.444, 5, '6', 7]
print(x)
print(type(x))
print(x[0])
'''print(x[100])
 # It will throw IndexError exception 'list index out of range'
 '''
print('Length of list :',len(x))

x.insert(1, "Neelesh")
print('Insert "Neelesh" at index 1', x)
print("Now lenght of list is", len(x))
x.insert(1, 1.001)
print('Insert "1.001" at index 1', x)
print("Now lenght of list is", len(x))
x.insert(1, 1100)
print('Insert "1100" at index 1', x)
print("Now lenght of list is", len(x))
x.insert(1, {1: 'value'})
print('Insert {1: "value"} at index 1', x)
print("Now lenght of list is", len(x))


x.remove({1: 'value'})
print("Remove ", x)

'''
If value is not in list it will throw ValueError: list.remove(x): x not in list
So how we can deal with this
'''
value = input('Find index of entered value from list: ')
try:
    indexofValue = x.index(value)
    print('index of {0} is {1}'.format(value, indexofValue))
except:
    print(value, 'is not found')



print("Now lenght of list is", len(x))
index = int(input("Enter the index which you want to remove from list: "))
try:
    value = x[index]
    print(' You have entered {0}th index,\n which has {1} value,\n Now your final list is {2}'.format(index, value, x))
    print("Now lenght of list is", len(x))
except:
    print("Index out of range")

    
