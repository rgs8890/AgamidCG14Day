# Loops allow us to repeat code wihtout manually writing code for each step
grocery_list = [
    {
        "name": "milk", "amount": 2, "cost": 2.5, "store": "Walmart",
    },
    {
        "name": "bread", "amount": 1, "cost": 1.5, "store": "Target",
    },
    {
        "name": "eggs", "amount": 12, "cost": 3, "store": "Costco",
    },
]

for item in grocery_list:
    print(f"{item["name"]} - {item["amount"]} units - ${item["cost"]}")

while True:
    command = input("Type a command add or done: ")
    if command == "done":
        break
    # If the command is not "done" it will assume the command is add

    name = input("Enter item name: ")
    amount = int(input("Enter amount: "))
    cost = float(input("Enter cost: "))
    store = input("Enter store: ")

    new_item_dict = {"name": name, "amount": amount, "cost": cost, "store": store}
    print(grocery_list)


