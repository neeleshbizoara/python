'''Module'''
print('Value of name is:', __name__)
x = 9
def funcname():
    print('Inside script')
    print(x)

funcname()

def oddEven(y):
    if(y%2 == 0):
        print('Even Number')
    else:
        print('Odd Number')

def sum(a,b):
    print('Sum is:', int(a)+int(b))

if __name__ == "__main__":
    print('In Module')


'''
Run following cmd:
python
import moduleName for example import seventhCalss
globals()


from moduleName import functionName
from moduleName import *
'''
