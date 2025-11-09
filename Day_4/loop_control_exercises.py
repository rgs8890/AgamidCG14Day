# TIP: The Operator in checks for memberships, You can use it to see if a string contains a specific substring or if the current item belongs to a list/set/dictionary
for item in ["apple", "banana", "chrrey", "mango"]:
    if item == "banana":
        pass
    print(item)

# Exercise 1
new_list = ["Djokovic", "Nadal", "Federer", "Murray", "Petros"]
for item in new_list:
    if item in new_list:
        pass
    print(item)

#Exercise 2
fruits = ["apple", "banana", "cherry", "kiwi"]
mixed_items = ["apple", "banana", "cherry", "onion", "aubergine", "tennis racket", "kiwi"]
for item in mixed_items:
    if item not in fruits:
        continue # Skips to the next item in the list and does not print it
    print(item)

print("\n")
# Exercise 3
for item in mixed_items:
    if item == "banana":
        pass
    print(item)
 # Pass allows the loop to continue, without taking action on specific items