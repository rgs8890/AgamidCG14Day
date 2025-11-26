# Large-Scale Apps, Games and Systems
# Make that chaos, make sense. Easier to debug, easier for other people to make sense.
# Core Principles -> how to make complex things manageable?

# Functionality, Control and Organisation
# OOP make objects work in the real-world
# An Object has its own thing that has properties and actions
# Pizza -> Bake, Slice and Serve.

'''
 :p Applications -> The Final Product
 :p Libraries & Frameworks -> Collections of modules/ packages
 :p Packages -> A Folder containing multiple modules with an __init__.py file
 :p Modules -> A Python File (.py) that groups related to classes and functions
 :p Classes -> Grouped data (attributes) and behaviour (methods)
 :p Functions & Methods -> Encapsulated logic that can be called multiple times
 :p Instructions -> Lowest level of code execution

'''
# 4 Pillars of OOP
# Encapulsation, Inheritance, Polymorphism, Abstraction
# Encapsulation -> Keeping details hidden and controlling access (Protects data in an object so only the right things can change it)

class Pizza:
    def __init__(self):
        self._toppings = [] # Use an underscore to indicate it is private
    
    def add_topping(self, topping):
        if topping not in self._toppings:
            self._toppings.append(topping)
            print(f"Added {topping}.")
        else:
            print(f"{topping} is already on the pizza")
    
    def remove_topping(self, topping):
        if topping not in self._toppings:
            self._toppings.remove(topping)
            print(f"{topping} has been removed")
        else:
            print(f"{topping} is already on the pizza")

    def show_toppings(self):
        if self._toppings:
            print("Current toppings:", ", ".join(self._toppings))
        else:
            print("No toppiungs yet.")
    
# Subclass for Pepperoni Pizza
class PepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.add_topping("pepperoni")
        self.add_topping("cheese")


class VeggiePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.add_topping("mushrooms")
        self.add_topping("onions")
        self.add_topping("green peppers")

# Inheritance lets you borrow things from another class

# Polymorphism is a way of saying many shapes, a small pizza or a large pizza -> action
# Cut -> each one cuts it differently

class LargePizza(Pizza):
    def __init__(self):
        super().__init__("Large")
    
    def cut(self):
        print("Cutting the large pizza into 8 slices.")

class SmallPizza(Pizza):
    def __init__(self):
        super().__init__("Small")
    
    def cut(self):
        print("Cutting the small pizza into 4 slices.")


# Abstraction -> hiding the complicated stuff
class Food:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def describe(self):
        return f"{self.name} is {self.color}"

apple = Food("Apple", "red")
banana = Food("Banana", "yellow")

print(apple.describe())
print(banana.describe())        

# Recreating the pizza class
class Pizza:
    
    def __init__(self, size, toppings, crust_type):
        self.size = size
        self.toppings = toppings
        self.crust_type = crust_type
    
    def bake():
        print("The pizza is currently being baked.")
    
    def slice(self):
        if self.size <= 4:
            print(f"Cutting the small pizza into {self.size} equal slices.")
        elif self.size > 4 and self.size <= 6:
            print(f"Cutting the medium size pizza into {self.size} equal slices.")
        else:
            print(f"Cutting the large size pizza into {self.size} equal slices.")
    
    def serve(self):
        print(f"Your pizza has been made. \n It contains {self.toppings} and is of {self.crust_type} \n. It also is a size of {self.size}")



