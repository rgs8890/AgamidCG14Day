# Methods and Classes
# These are just functions inside of a class which let objects do things within thier data
# methods belong to objects -> modules -> functions
# Functions withina  class that define behaviour of an object

class Shop:
    def __init__(self, orders):
        self.orders = []

    def add_order(self, drink):
        """Adds a drink to the order."""
        self.orders.append(drink)
        print(f"{drink} added to your order.")
    
    @classmethod # Class Methods -> work with the entire class
    def get_total_orders(cls):
        """Returns the total number of coffee orders created."""
        return cls.total_orders
    
    @staticmethod # Regular functions that work within a function
    def is_valid_drink(drink):
        """Checks if a drink name is (must be a non-empty string)"""
        return isinstance(drink, str) and bool(drink.strip())

# Method operates on a specific instance of a class
# They have self as their first parameter
# my_order = Shop()

class CoffeeOrder:
    total_orders = 0

    def __init__(self):
        self.orders = []
        CoffeeOrder.total_orders += 1
    
    @classmethod
    def get_total_orders(cls):
        '''Returns the total number of coffee orders created.'''
        return cls.total_orders

    def add_order(self, drink): # Instance method that adds a drink -> it appends by adding a new drink
        """Adds a drink to the order."""
        self.orders.append(drink)
        print(f"{drink} added to the order.")
    
    def cancel_order(self, drink):
        if drink in self.orders:
            self.orders.remove(drink)
            print(f"{drink} removed from the order.")
        else:
            print(f"{drink} not found in your order.")
        
    def show_order(self):
        """Displays all drinks in the order."""
        print("Your Order:" , ", ".join(self.orders))

    # Regular function which is logically grouped within the class for better organisation
    @staticmethod
    def is_valid_drink(drink):
        """Checks if a drink name is valid."""
        return isinstance(drink, str) and bool(drink.strip())

# Usage
#orders = ["Pot Noodles"]
my_order = CoffeeOrder()
my_order.add_order("Latte")
my_order.add_order("Espresso")
my_order.show_order()
my_order.cancel_order("Latte")
my_order.show_order()

# Instance Methods -> Each method requires "self" to access or modify the instance's state
# CLass Method works on the class level, and it aces on the entire class
# @classmethod -> decorator
# cls is taken as first parameter not 
print(CoffeeOrder.is_valid_drink("Capuccino"))
print(CoffeeOrder.is_valid_drink(""))

'''
:p Instance methods help and object store and change its own data
:p Class Methods work with the whole class, not just one object
:P Static Methods are like helpful functions within a class
'''

# Methods belong to objects
# What methods are?
# Why we use them?
# Different types of methods
# Functions of a class which define behvaiours of a project
