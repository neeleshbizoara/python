class Car:
    #pass
    def __init__(self, speed, color):  # It is not a constructor of the class but it behaves as constructor
        print('the __init__ is called')
        # speed = 0
        # color = 'White'
        self.speed = speed
        self.color = color
        print('Speed is {0} and color is {1}'.format(speed, color))

'''Create instance of class
when ever we create a instance of class it will init
In Python there is no distructor
self is like this key word'''
ford = Car(200, 'red') # parameters are required here as init method is decleared with these
honda = Car(220, 'Black')
audi = Car(250, 'White')


print(ford.speed , ford.color)

# ford.speed = 200 # Here speed is a attribute of created instance
# honda.speed = 220
# audi.speed = 250


# ford.color = 'red'
# honda.color = 'black'
# audi.color = 'white'

# print(ford.speed)
# print(ford.color)

# We can change value of instance attribute
ford.speed = 300
