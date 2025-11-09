grocery_list = [
    {"name": "milk", "store": "Walmart", "cost": 6.47, "amount": 2, "priority": 1, "buy": True},
    {"name": "bread", "store": "Walmart", "cost": 4.50, "amount": 2, "priority": 1, "buy": True},
    {"name": "eggs", "store": "Walmart", "cost": 5.00, "amount": 1, "priority": 1, "buy": True},
    {"name": "peanut butter", "store": "Costco", "cost": 12.50, "amount": 1, "priority": 3, "buy": True},
    {"name": "chicken", "store": "Costco", "cost": 25.00, "amount": 1, "priority": 2, "buy": True}
]

def add_item(name, store, cost, amount, priority, buy):
    item = {
        "name": name,
        "store": store,
        "cost": cost,
        "amount": amount,
        "priority": priority,
        "buy": buy
    }
    grocery_list.append(item)

def remove_item(name):
    for i, item in enumerate(grocery_list):
        if item["name"] == name:
            grocery_list.pop(i)
            return

def list_items():
    for item in grocery_list:
        print(item)

def get_index_from_name(name):
    for i, item in enumerate(grocery_list):
        if item["name"] == name:
            return i
    return None

def edit_item(name, store=None, cost=None, amount=None, priority=None, buy=None):
    index = get_index_from_name(name)
    if index is None:
        print(f"{name} not found.")
        return

    old_item = grocery_list[index]

    # Keep old values if new ones not provided
    new_item = {
        "name": name,
        "store": store if store is not None else old_item["store"],
        "cost": cost if cost is not None else old_item["cost"],
        "amount": amount if amount is not None else old_item["amount"],
        "priority": priority if priority is not None else old_item["priority"],
        "buy": buy if buy is not None else old_item["buy"]
    }

    grocery_list[index] = new_item

def export_items(round_cost=False):
    buy_list = [item for item in grocery_list if item["buy"]]

    if not buy_list:
        print("🛒 No items marked to buy.")
        return

    print("🛍️ Items to Buy:\n")
    total_cost = 0

    for item in buy_list:
        item_total = item["cost"] * item["amount"]
        total_cost += item_total
        cost_str = round(item["cost"], 2) if round_cost else item["cost"]
        print(f"name: {item['name']} | store: {item['store']} | cost: ${cost_str} | amount: {item['amount']}")
    
    #total_cost2 = calculate_total_cost(buy_list, round_cost = True)

    print("\n💰 Total estimated cost:", f"${round(total_cost, 2) if round_cost else total_cost}")
# --- demo ---
print("Before:", grocery_list)

add_item(name="apple", store="farmers market", cost=2.50, amount=8, priority=3, buy=False)
remove_item("bread")
edit_item(name="milk", store="Tesco", cost=5.99)

print("After:")
list_items()
