print("Hello World!")
# Data Types in Python -> Python Knows what we are working with
# Strings are just sequences of characters
print(1)
print(3.14)
print(True)
# Variables -> Containers to store data values -> store and reuse information 
# Comments explain what your code is doing
food = "Pizza"
print(food)
year = 2024 # Integer
pi = 3.14 # Float
print(year)

# Basic Operators
# +  -  *  /  % ** // Addition, Subtraction, Multiplication, Division, Modulus, Exponentiation, Floor Division
# == checks to see if both are equal
# Great for making decisions within the code
# More complex logic while you code
sum = 3 + 5
print(sum)
difference = 10 - 2
print(difference)

print(5>3)

print(True and False)
print(True or False)
print(not True)

# Python evaluates both sides of the equation before making a decision and returns the last value if both are TRUTHY Values
# Truthy Values are anything that is Not Zero, None or Empty Values

test_a = "pie" and "cake"
test_b = 300 and 9
test_c = "soda" and "taco" and "ice cream"
test_d = 7 and "orange"
print(test_a, test_b, test_c, test_d)

# AND returns the last truthy value if both are truthy else returns the first falsy value
# OR returns the first truthy value else returns the last falsy value if all are falsy

# String Concatenation

# Combining two or more strings
food = "pan" + "cake"
print(food)

food_a = "apple"
food_b = "pie"
combined_food = food_a +" " + food_b
print(combined_food)

favourite_food = "pizza"
my_favourite_food = "Your favourite food is" + " "
print(my_favourite_food + favourite_food)

# F-Strings -> Formatted Strings
favourite_food = "pizza"
food_output = f"Your favourite food is {favourite_food}"
print(food_output)

# string.replace(), string.upper(), string.lower()
store = "Walmart"
print(store.replace("Walmart", "Target"))

message = "I shop at the store"
print(message.replace("store", "Walmart"))

store = "Walmart"
print(store.upper())
print(store.lower())

message = "I shop at the store"
print(message.upper())

# favourite_food = input("What is your favourite food? ")
# print(f"You like {favourite_food}")

# Type Casting
num = int("10")
print(num)

cost = "7.54"
print(float(cost))

resultX = 7.50 + 8.43
print(resultX)
resultY = float("7.50") + float("8.43")
print(resultY)

str1 = "7.50"
str2 = "8.43"
print(str1 + str2) # these concatenate as all data types behave differently

#type_error_result = "7.50" + 7.50 # this will throw an error as you cannot concatenate different data types

# Dividing by 0 -> result divided by 0 will give you a zero division error
# Concatenating strings with numbers

# Version Control
# Track Changes, Go Back to Earlier Versions if needed, Rool back Versions, Collaborate, Time Machine for Code
# Important to collaborate with others; version control allows you for tracking
# can rewind and recover

# Git is a distributed working control system -> Each person gets their own copy of their puzzle
# Centralized system -> one thing that everyone is workingo n
# Tracking Changes -> Create own repository and manage projects with this