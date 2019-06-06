
false = False
if false:
    pass
else:
    print('Condition is false')

if 10 == 'true':
    print('int is equal to str')
else:
    print('int is not equal to str')

if 10 == int('10'):
    print('int is equal to str')
else:
    print('int is not equal to str')

print(''.isprintable())

x = int(input('Enter your age:'))
if x > 10 or x < 10:
    print('{0} is not equal to 10'.format(x))
    if x >= 22 and x <= 50:
        print('What is your source of income')
    else:
        print('You should takcare your self.')
else:
    print('your age is {0}'.format(x))


expression = x >= 22  and x<= 40
if expression:
    print('What is pass')
    pass