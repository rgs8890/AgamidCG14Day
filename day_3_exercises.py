# Exercise 1: Creating a Grocery List with Tuples
apples_tuple = ("apples", 0.50, 6)
bananas_tuple = ("bananas", 0.80, 9)
mangos_tuple = ("mangos", 1.00, 10)

grocery_list = []
grocery_list = [apples_tuple, bananas_tuple, mangos_tuple]
print(grocery_list)
print(grocery_list[0])
print(grocery_list[1])
print(grocery_list[2])

# One Method of Calculating Final Cost
total_cost = (apples_tuple[1] * apples_tuple[2]) + (bananas_tuple[1] * bananas_tuple[2]) + (mangos_tuple[1] * mangos_tuple[2])
print(total_cost)

# Another Method of Calculating Final Cost
total_cost_2 = sum([a[1]*a[2] for a in grocery_list])
print(total_cost_2)

for item in grocery_list:
    print(f"Total cost of {item[0]} is {item[1] * item[2]}")

# Exercise 2: Working with Dictionaries
apple_dict = {"name": "apple", "price": 0.50, "quantity": 5}
print(apple_dict)

bananas_dict = {"name": "bananas", "price": 0.80, "quantity": 9}
print(bananas_dict)

mangos_dict = {"name": "mangos", "price": 1.00, "quantity": 10}
print(mangos_dict)

list_dicts = [apple_dict, bananas_dict, mangos_dict]

for dict in list_dicts:
    dict["total_cost"] = dict["price"] * dict["quantity"]
    print(f"The total cost of {dict["name"]} is {dict["total_cost"]}")

# Exercise 3: Slicing and Sorting a List: Practice List Slicing, Sorting, Calculating Length
num_list = [16, 47, 1, 3, 5, 9, 15, 2]
print(num_list[2:])
print(num_list[4:])
print(num_list[-3]) # 3rd last item on the list

print(sorted(num_list, reverse=True))
print(len(num_list))

# Exercise 4: Sets Operations
daily_products = {'milk', 'butter', 'cream', 'yoghurt', 'cheese'}
desserts = {'jelly', 'chocolate', 'candy', 'cookies', 'muffins'}
print(daily_products)
print(desserts)
desserts.add('ice_cream')
daily_products.add('ice_cream')
print(desserts)

#daily_products.remove
daily_products.remove('butter')
print(daily_products)
desserts.remove('candy')
print(desserts)


intersect_items = daily_products.intersection(desserts)
print(intersect_items)