# Getters, Setters and Decorators when working with classes and functions
# Methods are functions which belong to objects
# How to use getters and setters
# Apply the @property decorator
# Use decorators to modify functions

'''
Getters, Setters
- This helps with security of the class
- COnstructor is what gets run as soon as a class instance is created
- Use this to safely read the attribute
- Setter method -> updates the value even if it is protected
- Grill Item -> Burger
- set_name -> updates the name to hot dog, this will print that
- if len(new_name) gets a new length
'''

'''
A protected attribute is an attribute which is intended to be accessed only within
the class and its subclasses.
- Not from outside the class
- Marked by a single _
- Only for internal use/ but does not enforce it
- protected attributes prevent accidental modification and encourage the use of getters nad setters
- like a do not touch sticker or something
- __private -> harder to access from outside the class

@property -> makes the getter look like a simple attribute
@name.setter -> makes it easier
'''

'''
A decorator is a function that wraps another function to ectend its behaviour without modifying the original code
-> it extends its behaviuors
-> my_decoroator -> wraps around extra code
-> now try stuff inside of the class
-> how long the function takes to run
-> Tracks grilling time
-> self.item stores the item (for use in other methods)
-> takes a function and returns a new wrapped version of it
-> Starts the timer, runs the original function then ends the original function
-> allows the method to be accessed as an attribute
-> indicate the grilling is done
-> creates a new instance for the grill item
'''

class GrillItem:
    def __init__(self, name):
        self.name = name

grill_item = GrillItem("Burger")
grill_item.name = "Hot Dog"

class GrillItem:
    def __init__(self, name):
        self._name = name
    
    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if len(new_name) > 0:
            self._name = new_name
        else:
            print("Grill Item name cannot be empty!")
    

grill_item = GrillItem("Burger")
grill_item.set_name("")
grill_item.set_name("Hot Dog")
print(grill_item.get_name())

# The setter allows us to set the name and validate before setting, so we don;t try to set it to something that might cause issues, like an emptry string
# The getter gets the value without tampering with the attribute directly

'''
What is a protected attribute?
- Starts with one underscore (e.g. _name)
- Isn't truly private but signals: "Don't touch unless you know what you're doing"
- Encourages use of getters and setters

A private attribute:
- Has a double underscore(__name) which makes it even more private
- Doing this will automatically modify the attribute to something like
_ClassName__name which is name mangling; making it more difficult to access from
outside of the class
'''

class GrillItem:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if len(new_name) > 0:
            self._name = new_name
        else:
            print("Grill Item name cannot be empty!")
    
grill_item = GrillItem("Burger")
print(grill_item.name)
grill_item.name = "hot Dog"
grill_item.name = ""

# Decorators: Functions that modify functions
# A decorator is a function that wraps another function to add behaviour, like logging, timing, or validation

def my_decorator(func):
    def wrapper():
        print("Before grilling...")
        func()
        print("After grilling....")
    return wrapper

@my_decorator
def grill_burger():
    print("Grilling the burger!")

grill_burger()

# Decorator inside of a class
import time

class GrillTimer:
    def __init__(self, item):
        self.item = item
    
    def timer_decorator(self, func):
        def wrapper():
            start = time.time()
            func()
            end = time.time()
            print(f"Grilling time for {self.item}: {end-start} seconds")
        return wrapper

    @property
    def grill(self):
        @self.timer_decorator
        def slow_grill():
            time.sleep(2)
            print(f"{self.item} is ready!")
        return slow_grill
    
grill_item = GrillTimer("Burger")
grill_item.grill()

# Instance Methods
# Operator on a specific instance (object) of a class
# Can access and change instance attributes

class CoffeeOrder:
    def __init__(self):
        self.orders = []

    def add_order(self, drink):
        self.orders.append(drink)
        print(f"{drink} added to your order.")
    
    def cancel_order(self, drink):
        if drink in self.orders:
            self.orders.remove(drink)
            print(f"{drink} removed from your order.")
        else:
            print(f"{drink} not found in your order.")
    
    def show_order(self):
        print("Your order:", ", ".join(self.orders))


# Interview Question
'''
1. How have I used getters and setters within my code?
'''