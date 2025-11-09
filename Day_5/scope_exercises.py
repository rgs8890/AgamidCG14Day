# Variable scope and lifetime help us control where and how long variables are accessible in our code. This can prevent errors and improve code organisation

# Global Scope: Variables defined outside of any function or block. Accessible throughout the program.
message = "I love chocolate!"
def chocolate():
    print(message)

chocolate()
print(message) #  this will not show an error -> as this is a global variable

# Lifetime refers to how long a variable exists in memory
# Global Variables exist throghout the entire runtime of the program
# Local Variables only exist during the execution of the function in which they are defined; once the function completes, these variables are discarded

# Exercise 1: Local and Global Variables
food = "Pizza"

def favourite_food():
    food = "Sushi"
    print("Local Food:", food)

favourite_food()
print("Global Food:", food)

# Exercise 2: Variable LifeTime in Functions
def counter():
    count = 0
    count += 1
    print("Count:", count)

counter()
counter()

# Exercise 3: Combining Scope and Lifetime
user_name = "Skyler"

def change_name():
    user_name = "sfines"
    print("Inside Function:", user_name)

change_name()
print("Outside function:", user_name)