# GLOBAL VARIABLES and Constants
# Global Variables: Can make code harder to understand and maintain. 
# It's best to avoid global variables, as they can be accessed and modified
# from anywhere in the code.

# Pass variables in a class or function, so we know where they come from.
# Constants: Use ALL_CAPS for constants to indicate they should not be changed.
PI = 3.14159  # Constant
MAX_USERS = 100  # Constant
user_count = 0  # Global Variable

#BC_TAX -> CONSTANTS : We only change the value in one place
# Add constants at the top of your code
# Constants are all in capitals -> typings and annotations -> to clarify 
# what each part of the code does

# Best Practices
# Pass Variables as Arguments: Instead of relying on global variables, pass the required values directly to functions
def multiply_by_two(num):
    return num * 2

# Encapsulate Variables in Functions or Classes: Keep variables loval to their specific function or clas
number = 10
result = multiply_by_two(number)
print(result)


def calculate_area(length, width):
    area = length * width
    return area

length = 5
width = 10
result = calculate_area(length, width)
print(result)

# Using Constants
MAX_CONNECTIONS = 5 # ALL CAPS shows the reader these values will not change
TIMEOUT = 30

def connect():
    for i in range(MAX_CONNECTIONS):
        print("Connecting...")
#Constants be at the top of the file