'''Function can be 2 type
 Built in function for example print(), input(), min()
 User defined function

def nameOfFunction(arg1, arg2, arg3):
     #statemnt
     print('')

nameOfFunction(1,2,3)
'''

def sum(arg1, arg2):
    if type(arg1) != type(arg2):
        print("Please give the args of same type")
        return # Because here we return nothing so when this statment will execute it will return None
    return (arg1+arg2)

a = sum(15,60)
print(a)
print(sum('Hello', 'World'))
print(sum(15.678, 80.234))
print(sum('Hello', 15))