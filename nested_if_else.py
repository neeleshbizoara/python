name = input('Enter you name:')

if len(name) < 8:
    print("Name Entered is: ", name, ", it should be min 8 characher.")
elif name.islower():
    print('Atleast one character should be in upper case.')
elif name.isupper():
    print('Atleast one character should be in lower case.')
elif name.isspace():
    print('Will not accept space')
else:
    print("Congratulation!", name)



''' Even Odd '''

x = input("Enter any number:")
if type(x) == str:
    print("It is string, so convert to int")
    y = int(x)
    if y < 0:
        print("Entered number is negative")
    elif y != 0:
        if (y % 2) == 0:
            print("Entered number is even.")
        else:
            print("Entered number is odd.")
    else:
        print("You have entered 0 which is even")
else:
    print("It is int")

