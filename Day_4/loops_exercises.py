# Loops allow repetice execution of code blocks. Use for to iterate over sequences and while to repeat until a condition is false
# Exercise 1:
grocery_list = ["chocolate", "muffin", "pizza", "chips", "curry", "chapatti", "paneer butter masala", "bread"]
for item in grocery_list:
    print(item)

# Exercise 2
while True:
    condition = input("Add or Done?").lower()
    if condition == "done":
        break
    elif condition == "add":
        item_to_add = input("Please enter item to add to grocery list: ")
        grocery_list.append(item_to_add)
        print(grocery_list)
    else:
        print("Invalid entry. Please type Add or Done.")

# Exercise 3
grocery_dict = [
    {
        "name": "chocolate", "cost": 3.45,
    },
    {
        "name": "muffin", "cost": 4.50,
    },
    {
        "name": "pizza", "cost": 6.00,
    },
    {
        "name": "chips", "cost": 2.50,
    },
    {
        "name": "curry", "cost": 5.00,
    },
    {
        "name": "chapatti", "cost": 6.00,
    },
]
for item in grocery_dict:
    print(f"{item["name"]} and {item["cost"]}")