'''Multi-Line Text, Comments, F-Strings'''
# Understanding how to manage multi-line texts, comments and complex 
# experessions is essential for writing clean and efficient Python code.

# Multi-Line Strings
"""
Python provides two simple methods for keeping things tidy:
- Parantheses
- Triple Quotes
"""

# Parantheses
long_string = (
    "If we put out text in paranthesis"
    "We can write multi-line strings"
    "This saves us space and keeps things clean"
)
print(long_string)

# Triple Quotes
long_string = """
Triple quotes give us more control:
1. The text output will appear as is
2. This makes it more predictable
3. Making it easier to maintain formatting
"""
print(long_string)

# Multi-Line Function Calls
add_item(
    name = "Kiwis",
    store = "Costco", 
    cost = 10.50, 
    amount = 2, 
    priority = 2, 
    buy = True)
# This structure makes it easier to scan and debug functions, especially when the arguments are complex

# Multi-Line Data Structures
# Large Data structures like Lists and Dictionaries from being split across multiple lines
grocery_list ={}

add_item_to_grocery_list(
    grocery_list,
    name = "Kiwis",
    store = "Costco", 
    cost = 10.50, 
    amount = 2, 
    priority = 2, 
    buy = True
)

# Example Grocery List of Dictionaries
grocery_list = [
    {
        "name": "Bread",
        "store": "Walmart",
        "cost": 4.50,
        "amount": 1,
        "priority": 1,
        "buy": True
    },
    {
        "name": "Cheese",
        "store": "Target",
        "cost": 12.47,
        "amount": 1,
        "priority": 2,
        "buy": True
    },
    {
        "name": "Yoghurt",
        "store": "Costco",
        "cost": 3.99,
        "amount": 6,
        "priority": 3,
        "buy": True
    }
]

# F-Strings with Multi-Line Expressions
result = "{name} costs ${cost:.2f} at {store}".format(name, cost, store)
print(result)

result = f"{name} costs ${cost:.2f} at {store}"
print(result)

# F Strings make this easier to call
# Make long code lines shorter and more readable

# Multi Line Data Structures
grocery_items = ["Apples", "Bananas", "Carrots","Dates", "Eggplants", "Figs", "Potatoes", "Chocolate"]
grocery_items = [
    "Apples", 
    "Bananas", 
    "Carrots",
    "Dates", 
    "Eggplants", 
    "Figs", 
    "Potatoes", 
    "Chocolate"
]

# Dictionaries
grocery_item = {"name": "chicken", "store": "Walmart", "cost": 5.99, "amount": 2, "priority": 1, "buy": True}

# Multi-Line Dictionary
grocery_item = {
    "name": "chicken", 
    "store": "Walmart", 
    "cost": 5.99, 
    "amount": 2, 
    "priority": 1, 
    "buy": True
}

# Multi-Line Comments
"""
Triple quotes are often used as workaround for multi-line comments.
They are multi-line strings, but Python ignores them if not assigned
to a variable.
"""
print("Code runs normally.")

# Module Docstrings
"""
grocery_module.py
-----------------
A simple grocery management module that supports adding, editing, removing,
and exporting grocery list items.

This module demonstrates the use of functions, lists, and dictionaries
to manage shopping data — as well as best practices such as using
try-except blocks, input validation, and module-level documentation.

Author: Rohit Sunku
Version: 1.0
Date: November 2025
License: MIT
"""