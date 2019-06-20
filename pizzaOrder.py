class PizzaOrder:
    '''This class is for Pizza Order'''
    orederNumber = 0
    pizzaNames = ["margherita", "cornNonion", "onionCapsicumTomato"]
    pizzaCrusts = ['HandTossed', 'ThinCrust', 'CheezeBurst', 'NewHandTossed']
    pizzaToppings = ['Onion', 'Tomato', 'Capsicum' ]
    OrderStatus = ['recieved', 'preperation', 'baking', 'outForDelivery', 'Delivered']

    def incrementOrderNumber(self):
        PizzaOrder.orederNumber += 1
        return PizzaOrder.orederNumber

    
    def __init__(self, name, mobileNumber, pizzaName, pizzaCrust, pizzaToppings):
        self.name = input('What is your name:')
        self.mobileNumber = int(input('What is your mobile number'))
        self.pizzaName = pizzaName
        if self.pizzaName not in PizzaOrder.pizzaNames:
            print("Wrong pizza name, choose among below names:")
            print(PizzaOrder.pizzaNames, sep="::")
            raise Exception

        self.pizzaCrust = input('Enter crust')
        if self.pizzaCrust not in PizzaOrder.pizzaCrusts:
            print("Wrong pizza Crust, choose among below Crust:")
            print(PizzaOrder.pizzaCrusts, sep = "::")
            raise Exception
            
        self.pizzaToppings = input('Enter Topping list').split(' ')
        for x in self.pizzaToppings:
            if x not in PizzaOrder.pizzaToppings:
                print("Wrong pizza Topping, choose among below Crust:")
                print(PizzaOrder.pizzaToppings, sep = "::")
                raise Exception
            
        self.orderId = self.incrementOrderNumber()

    
x = PizzaOrder('Neelesh', '7218718108', 'CheezeCorn','CheezeBurst', ["Onion", "Tomato"])
print(x.name)