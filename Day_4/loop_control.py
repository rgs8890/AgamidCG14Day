# Loop Control
# Break lets you stop early. Break lets you stop a loop when something happens

grocery_list = ["milk", "bread", "eggs", "cheese", "apples", "bananas"]

item_to_find = "cheese"

for item in grocery_list:
    if item == item_to_find:
        print(f"Found {item_to_find}")
    else:
        print(f"{item_to_find} not in grocery list.")

for item in grocery_list:
    if item in grocery_list:
        continue # skips to the next item

for item in grocery_list:
    if item in grocery_list:
        pass # I will handle this later, run the other code