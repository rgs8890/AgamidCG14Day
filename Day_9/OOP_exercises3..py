# Getters, Setters and Decorators
# Working with classes, functions and methods

# Functions -> Modules <- Objects -> Methods

# How to use getters and setters
# Apply the @property decorator

# Use decorators to modify functions
# Data Protection is Key -> Class Attributes

class GrillItem:
    def __init__(self, name):
        self.name = name

grill_item = GrillItem("Burger")
print(grill_item.name)
grill_item.name = "Hot Dog"
