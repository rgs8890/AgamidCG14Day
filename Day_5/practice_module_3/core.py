grocery_list = [
    {
        "name": "milk", "store": "Walmart", "cost": 6.47, "amount": 2, "priority": 1, "buy": True
    },
    {
        "name": "curry", "store": "Cash & Carry", "cost": 7.58, "amount": 3, "priority": 2, "buy": False
    },
    {
        "name": "pot noodles", "store": "Cash & Carry", "cost": 6.47, "amount": 2, "priority": 1, "buy": True
    },
    {
        "name": "computer", "store": "Computer Store", "cost": 250, "amount": 1, "priority": 2, "buy": False
    },
    {
        "name": "biriyani", "store": "Indian Curries", "cost": 10, "amount": 5, "priority": 3, "buy": True
    }
]

def add_item(name, store, cost, amount, priority, buy, category = None, expiration_date = None):
    item = {"name": name, "store": store, "cost": cost, "amount": amount, "priority": priority, "buy": buy, "category": category, "expiration_date": expiration_date}
    grocery_list.append(item)

def search_item(name):
    try:
        index = get_index_from_name(name)
        item = grocery_list[index]
        return item
    except IndexError:
        print("Item is not found.")
        return None

def remove_item(name):
    index = get_index_from_name(name)
    
    grocery_list.pop(index)

def get_index_from_name(name):

    index = 0

    for item in grocery_list:
        if item["name"] == name:
            return index
        else:
            index += 1

# fruits = ["apple", "banana", "cherry"]

# for index, fruit in enumerate(fruits):
#     print("The index of {fruit} is {index}")

def edit_item(name, store = None, cost = None, amount = None, priority = None, buy = "skip"):

    index = get_index_from_name(name)

    old_item = grocery_list[index]

    if not store:
        store = old_item["store"]
    
    if not cost:
        cost = old_item["cost"]
    
    if not amount:
        amount = old_item["amount"]

    if not priority:
        priority = old_item["priority"]
    
    if buy == "skip":
        buy = old_item["buy"]
    
    
    item = {"name": name, "store": store, "cost": cost, "amount": amount, "priority": priority, "buy": buy}

    grocery_list[index] = item

def list_items():
    for item in grocery_list:
        print(item)

def calculate_total_cost(list, round_cost = True):
    total_cost = 0
    for item in list:
        if round_cost:
            total_cost += round(item["cost"] * item["amount"])
        else:
            total_cost += (item["cost"] * item["amount"])
    return total_cost
    

def export_items():
    buy_list = []

    for item in grocery_list:
        if item["buy"]:
            buy_list.append(item)

    if buy_list:
        for item in buy_list:
            print(f"name: {item['name']} - store: {item['store']} - cost: ${item['cost']} - amount: {item['amount']} - priority: {item['priority']}")

        total_cost = calculate_total_cost(buy_list, round_cost=True)

        print(f"The total cost is ${total_cost}")
    
print("grocery list before: ")
list_items()

add_item('bread', 'Costco', 3.0, 1, 2, False)
print("Grocery List After:")
list_items()