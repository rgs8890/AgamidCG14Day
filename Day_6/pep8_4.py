# Single responsibility Principle

# Non SRP
def make_sandwich(bread, fillings, condiments):

    ingredients = [bread]
    ingredients.extend(fillings)
    ingredients.extend(condiments)

    sandwich = f"{ingredients[0]} with " + ", ".join(ingredients[1:])

    print(f"Here is your sandwich: {sandwich}")

bread = "Whole grain"
fillings = ["Turkey", "Cheese"]
condiments = ["Mayo", "Mustard"]
make_sandwich(bread, fillings, condiments)

# SRP Example:
def gather_ingredients(bread, fillings, condiments):

    ingredients = [bread]
    ingredients.extend(fillings)
    ingredients.extend(condiments)

    return ingredients


def assemble_sandwich(ingredients):

    sandwich = f"{ingredients[0]} with " + ", ".join(ingredients[1:])
    
    return sandwich

def present_sandwich(sandwich):

    print(f"Here is your sandwich: {sandwich}")

def make_sandwich(bread, fillings, condiments):
    
    ingredients = gather_ingredients(bread, fillings, condiments)
    sandwich = assemble_sandwich(ingredients)
    present_sandwich(sandwich)


# Keeping Functions Short -> Improve readability and ease of debugging
# If a function exceeds 20 lines, think about how to break it into smaller, focused functions

# constants.py -> All in capital letters
TAX = 0.12
ERROR_ITEM_NOT_FOUND = "Error: Item not found in inventory"
ERROR_INVALID_QUANTITY = "Error: Invalid quantity provided"

APP_NAME = "Grocery List App"
VERSION = "1.0.0"
AUTHOR = "Skyler Fines"

CATEGORIES = ["Fruits", "Vegetables", "Dairy", "Meat", "Beverages"]

DEFAULT_RESTOCK_QUANTITY = 10

DEFAULT_ITEMS = {
    "apples": 10,
    "bananas": 8,
    "oranges": 2,
}

# Using a Top-Down Approach
# Purpose: Help readers understand the high-level structure before diving into details

# Main Functions: These functions orchestrate the overall logic of the program. 
# They call helper functions to perform specific tasks, handle the program's flow 
# interact with the user

# Helper Functions: Smaller, modular functions designed to perform specific tasks
# Main function
def manage_shopping_cart():
    """Main function to manage the shopping cart."""
    items = ["Banana", "Apple", "Carrot"]
    prices = [0.99, 1.49, 0.79]
    
    sorted_items = sort_list(items)  # Calls helper function
    total_cost = calculate_total_cost(prices)  # Calls helper function
    
    print("Shopping Cart:")
    for item, price in zip(sorted_items, prices):
        print(f"{item}: ${price:.2f}")
    print(f"Total Cost: ${total_cost:.2f}")

# Helper functions
def sort_list(items):
    """Sort a list of items."""
    return sorted(items)

def calculate_total_cost(prices):
    """Calculate the total cost of items."""
    return sum(prices)

# Run the main function
manage_shopping_cart()

# Example
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

zipped = zip(list1, list2)
print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# Encapsulating data in methods and classes 
class GroceryList:
    def __init__(self):
        """Initialize an empty grocery list."""
        self.items = []

    def add_item(self, item, quantity):
        """Add an item to the grocery list."""
        self.items.append({'item': item, 'quantity': quantity})

    def remove_item(self, item):
        """Remove an item from the grocery list if it exists."""
        self.items = [i for i in self.items if i['item'] != item]
    
    def edit_item(self, item, new_quantity):
        """Edit an item of the grocery list."""
        for entry in self.items:
            if entry['item'] == item:
                entry['quantity'] = new_quantity
                break
    
    def list_items(self):
        """Return the list of items in the grocery list."""
        return self.items

    def display_items(self):
        """Display all items in the grocery list."""
        for entry in self.items:
            print(f"{entry['quantity']} x {entry['item']}")

