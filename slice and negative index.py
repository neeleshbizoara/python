a = [0,1,2,3,4,5,6,7,8,9] #It is a list
b = (0,1,2,3,4,5,6,7,8,9) #It is a tuple
c = '0123456789' #It is a string

# x = slice(start, end, stpe)
print(a)
x = slice(0,5) # end will not consider
print(a[x])

#another way to slice
print(a[0:6])

# a[start:end]   # items start through end-1
# a[start:]      # items start through the rest of the array
# a[:end]        # items from the beginning through end-1
# a[:]           # a copy of whole array
#a[start:end:step]  # start through not past end, by step
print('slice operation on list')
print(a)
print(a[4:])
print(a[:4])
print(a[:])
print(a[2:7:2])
print(a[::3])

print('slice operation on tuple')
print(b)
print(b[4:])
print(b[:4])
print(b[:])
print(b[2:7:2])
print(b[::3])

print('slice operation on string')
print(c)
print(c[4:])
print(c[:4])
print(c[:])
print(c[2:7:2])
print(c[::3])

'''Python has alos negative index'''
print(c)
print(c[-1])
print(c[::-1]) #It will return string in reverse order
print(a[-4::-1])
print(b[:-4:-1])
print(b[-4::-1])