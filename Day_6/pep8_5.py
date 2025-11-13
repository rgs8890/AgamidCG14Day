# Look before you LEAP
grocery_list = {
    "apples": 4,
    "bananas": 3,
    "milk": 2,
}


# LBYL Approach -> Proacvie -> Ideal for predicatable scenarios 
# provides more control over code
# When pre-checking is quick and straightforward
# To prevent predictable errors like accessing an item in a grocery list 
# that might not exist
if "eggs" in grocery_list:
    print(f"Eggs: {grocery_list["eggs"]} units")
else:
    print("Error: 'eggs' not found in grocery list.")

# EAFP Approach -> Reactive -> Pythonic way
# Useful when pre-checking is complex or time-consuming
# Allows flecibility when checking new code

try:
    print(f"Eggs: {grocery_list['eggs']} units")
except KeyError:
    print("Error: 'eggs' not found in grocery list.")

