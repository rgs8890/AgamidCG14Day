# Exercise 1: Grocery Item Categorization Using Conditional Statement
item = input("Please input a grocery item: ").lower()

food_items = ["apple", "bread", "milk", "cheese", "wangi-bath", "bisabilibath", "biriyani", "idli", "vada"]
non_food_items = ["soap", "detergent", "paper towels", "dj", "speakers"]

if item in food_items:
    food_items.append(item)
    print("This is a food item.")
elif item in non_food_items:
    non_food_items.append(item)
    print("This is not a food item.")
elif item == "onlyfans":
    print("Mate, get to the gym, get into shape, and start approaching real women. It is not that hard.")
else:
    print("Unknown Item")


# Exercise 2, 3, 4, 5: Making a Burger with a While Loop
# Make burgers and fries for you and your friends, but you only have $27.50
# Let us make burgers and fries with the budget

items_list = [
    {"name": "fries", "cost":6.25, "amount": 1},
    {"name": "burger patties", "cost":13.50, "amount": 1},
    {"name": "burger buns", "cost":3.50, "amount": 2},
    {"name": "tomato", "cost":1.50, "amount": 2},
    {"name": "lettuce", "cost":5, "amount": 1},
    {"name": "Ketchup", "cost":3.47, "amount": 1},
    {"name": "pickles", "cost":4.25, "amount": 1}
]

shopping_list = []
budget = 27.50
total_cost = 0
index = 0
while (total_cost <= budget and index < len(items_list)):
    item = items_list[index]
    if total_cost + (item["cost"] * item["amount"]) > budget:
        break 
    shopping_list.append(item["name"])
    total_cost += (item["cost"] * item["amount"])
    if ( 
        "burger buns" in shopping_list
        and "fries" in shopping_list
        and "burger patties" in shopping_list
    ):
        print(f"We can make burgers and fries for {total_cost}!") # Exercise 4
        break
    try: # Exercise 5
        index += 1
    except:
        print("The index must be an integer")
        break
    for item in shopping_list:
        print(item) # Exercise 3
    print('----------')

print("🛒 Shopping list:", shopping_list)
print(f"💰 Total cost: ${total_cost:.2f}")
print(f"Remaining budget: ${budget - total_cost:.2f}")

# Exercise 5 - Own Version
# Get used using try-except blocks to handle errors
items_list2 = [
    {"name": "tortillas", "cost":6.25, "amount": 1},
    {"name": "chicken", "cost":13.50, "amount": 1},
    {"name": "peppers", "cost":3.50, "amount": 2},
    {"name": "onions", "cost":1.50, "amount": 2},
    {"name": "tortilla mix", "cost":5, "amount": 1},
    {"name": "mushrooms", "cost":3.47, "amount": 1},
    {"name": "pickles", "cost":4.25, "amount": 1}
]

index2 = 0
budget2 = 32.50
shopping_list2 = []
total_cost2 = 0
print("I'm Making tortillas!")
while (total_cost2 <= budget2 and index2 < len(items_list2)):
    item = items_list2[index2]
    if total_cost2 + (item["cost"] * item["amount"]) > budget2:
        break
    shopping_list2.append(item["name"])
    total_cost2 += item["cost"] * item["amount"]
    if ("tortillas" in shopping_list2
        and "chicken" in shopping_list2
        and "peppers" in shopping_list2):
            print(f"We can make tortillas for {total_cost2}!")
            break

    try:
        index2 += 1
    except:
        print("The index must be an integer")
        break
    for item in shopping_list2:
        print(item)
    print("-----------")

print("🛒 Shopping list:", shopping_list2)
print(f"💰 Total cost: ${total_cost2:.2f}")
print(f"Remaining budget: ${budget2 - total_cost2:.2f}") 