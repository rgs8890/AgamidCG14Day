def write_grocery_list():

    grocery_list = ["carrots", "bananas", "apples", "pears", "beans", "bread"]

    with open("grocery_list.txt", "w") as file:
         for item in grocery_list:
              file.write(item + "\n")
        
    print("Grocery list written in file.")

write_grocery_list()

with open("grocery_list.txt", "a") as file:
     file.write("Eggs\n")

with open("grocery_list.txt", "r") as file:
     for line in file:
          print(line)

# Exercise 5
try:
    write_grocery_list()
except PermissionError as pe:
    print("Error: You do not have the necessary permissions.")