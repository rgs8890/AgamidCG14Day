# Parameters customize functions and give you something back
# Parameters and Return Values
# A parameter is like an ingredient into your function
# Return -> bit like a vending machine

def calculate_total_cost(grocery_list, round_cost = True, tax = 0.12):
    total_cost = 0

    for item in grocery_list:
        cost = item["amount"] * item["cost"]
        total_cost += cost
    
    if round_cost:
        total_cost = round(total_cost)
    
    if tax:
        tax_cost = total_cost * tax
        total_cost += tax_cost

    print(f"The total cost is {total_cost}")
    return total_cost

grocery_list_a = [{
    "name": "apple", "cost": 2.37, "amount": 6
},
{
    "name": "banana", "cost": 0.79, "amount": 12
},
{
    "name": "strawberris", "cost": 10.25, "amount": 10
}]

grocery_list_b = [
    {
        "name": "bread", "cost": 3.75, "amount": 1
    },
    {
        "name": "milk", "cost": 6.50, "amount": 1
    },
    {
        "name": "eggs", "cost": 4., "amount": 1
    }
]

grocery_list_a_cost = calculate_total_cost(grocery_list_a)
grocery_list_b_cost = calculate_total_cost(grocery_list_b)
print(f"This is the value of grocery list a ${grocery_list_a}")
print(f"This is the value of grocery list b ${grocery_list_b}")
combined_value = grocery_list_a_cost + grocery_list_b_cost
print(f"The combined cost of list a and list b is ${combined_value}")

# Parameters let you customize what your function does based on input
# Return values give you something back after your function runs

