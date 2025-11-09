# Handling Errors
# Python tells me what exactly went wrong and where to look


# Troubleshooting
# A detailed traceback of what happened
pizza_price = 32.57
people = 3
cost_per_person = pizza_price / people
print(f"Each person needs to pay: ${cost_per_person}")

# Errors should be descriptive and controlled by their developer
# TRY-EXCEPT - A great tool when you kow the error that will be triggered
try:
    cost_per_person = pizza_price / people
    print(f"Each person needs to pay: ${cost_per_person}")
except ZeroDivisionError:
    print("ERROR: you need to have at least one person to calculate the pizza cost.")

# When the conditons never change
grocery_list = ["apple", "burger buns", "hotdog", "milk", "bread", "coffee", "juice"]
number_of_items = 0
while number_of_items < 5:
    print("Adding items to the list.")
    number_of_items +=1
