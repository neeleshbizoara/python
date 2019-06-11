i = 0

while i < 5:
    print('The value of i is',i)
    i +=1 #i++
    pass # Python 3 - pass Statement. It is used when a statement is required 
         # syntactically but you do not want any command or code to execute.
         # The pass statement is a null operation; nothing happens when it executes.
print('Finished while loop')

# While else loop example
num = 1
sum = 0
print('Enter a Number. Please enter zero(0) to exit')

while num != 0:
    num = float(input("Number ? "))
    sum = sum + num
    print("Sum = ",sum)
else:
    print('Finished sum')

# Iwill execute for ever as condition is always true
'''
while True:
    print('The value of i is',i)
    i +=1 
print('Finished while loop')
'''

