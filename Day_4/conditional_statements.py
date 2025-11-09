# Conditional Statements
# IF/ELSE/ELIF
# Helps your code make decisions based on the different conditions
# Loops - Repeatable actions
# For, While
# Loop Control
# Break, Continue, Pass
# Debugging and Error Handlign
# Try, Except
# Make code more flexible, dunamic and resilient
# Python chooses what to do based on different conditions

# IF statements are like asking your code a question
# ELSE is like the back up plan
tomato_dict = {
    "name": "tomato",
    "cost": 2.25,
    "amount": 3,
    "backup": "canned tomato",
    "available": True
}
print(tomato_dict)
tomato_dict["available"] = False

if tomato_dict["amount"] < 5 and not tomato_dict["available"]:
    select_item = "cherry items"
    select_amount = 1
elif tomato_dict["amount"] >= 5 and not tomato_dict["available"]:
    select_item = tomato_dict["backup"]
    select_amount = 1
    if tomato_dict["amount"] > 5:
        select_amount = tomato_dict["amount"] / 5
else:
    select_item = tomato_dict["name"]
    select_amount = tomato_dict["amount"]

print(select_item)
print(f"Lets buy {select_item} {select_amount}")

tomato = True
num_tomatoes = 5
cost = 2.50

if tomato:
    print("We only got to tomato!")
elif num_tomatoes < 6:
    print("We got to num tomatoes")
elif cost == 2.50:
    print("We got to cost")
else:
    print("None of these1")

# IF statements are like asking your code a question
# ELIF lets you handle multiple possibilities
# ELSE is like your backup plan