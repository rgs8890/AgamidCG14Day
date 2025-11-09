# What are parameters?
# Parameters are like placeholders in a function definition that let us pass data into the function. They help functions be more flexible
# and useful by allowing them to work with different inputs each time we call them

# Exercises
# Grocery list
grocery_list = [
    {"name": "Orange Juice", "amount": 5, "available": True, "location": "Store"},
    {"name": "Bread", "amount": 10, "available": False, "location": "Store"},
    {"name": "Chips", "amount": 15, "available": False, "location": "Store"},
    {"name": "Cookies", "amount": 0, "available": False, "location": "Store"},
    {"name": "Milk", "amount": 100, "available": True, "location": "Dairy Aisle"},
    {"name": "Apples", "amount": 40, "available": False, "location": "Produce Section"},
]


def print_list_grocery_items(grocery_list):
    print(grocery_list)


def find_item(name_item, is_available):
    for item in grocery_list:
        if item["name"] == name_item:
            if is_available and item["available"]:
                return f"{name_item} is available."
            else:
                return f"{name_item} is not available."
    return f"{name_item} not found."


def favorite_snack(snack_name, quantity_left):
    for item in grocery_list:
        if snack_name == item["name"]:
            # enough in stock
            if item["amount"] >= quantity_left and item["amount"] != 0:
                return f"You have {item['amount']} of {snack_name} left!"
            # none in stock
            elif item["amount"] == 0:
                return f"You are out of {snack_name}!"
            else:
                return "There is less than the quantity you have demanded."
    return "That snack is not in the list."


def item_location(item_name, store_section):
    for item in grocery_list:
        if item_name == item["name"]:
            if store_section == item["location"]:
                return f"Found {item_name} in {store_section}"
            else:
                return f"Found {item_name} in a different location: {item['location']}"
    # only if we never found it
    return f"Cannot find {item_name}"


# Tests
print(find_item("Orange Juice", True))       # Orange Juice is available.
print(find_item("Bread", False))             # Bread is not available.

print(favorite_snack("Chips", 3))            # You have 15 of Chips left!
print(favorite_snack("Cookies", 0))          # You are out of Cookies!

print(item_location("Milk", "Dairy Aisle"))  # Found Milk in Dairy Aisle
print(item_location("Apples", "Produce Section"))  # Found Apples in Produce Section
