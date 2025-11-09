# Day 4: Error Handling and Debugging
# TRY and EXCEPT
# Error Handling allows you to manage program errors gracefully using try and except. Debugging includes reading error messages (tracebacks) and solving
# errors (infinite loops)

# Exercise 1
user_input = input("Please Enter a number: ")
try:
    value = float(user_input)
    print(value)
except ValueError:
    print("Cannot convert user_input to float.")


# Exercise 2
a = 10
b = 5

# Step 1: Attempt to double the value of 'b' by assigning it to 'double_b'
double_b = b * 2

# Step 2: Try to add 'a' and 'double_b' and store the result in 'total'
total = a + double_b

print("The total is:", total)