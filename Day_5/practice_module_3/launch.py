import core

def launch():
    while True:
        command = input("Enter a command (add, remove, edit, search, list, export, quit): ")

        if command == "add":
            name, store, cost, amount, priority, buy = get_inputs()
            core.add_item(name = name, store = store, cost = cost, amount = amount, priority = priority, buy = buy)
        
        if command == "remove":
            name = input("Item to remove:")
            core.remove_item(name)
        
        if command == "edit":
            name, store, cost, amount, priority, buy = get_inputs()
            core.edit_item(name = name, store = store, cost = cost, amount = amount, priority = priority, buy = buy)
        
        if command == "search":
            name = input("Item to search:")
            itemX = core.search_item(name)
            print(itemX)

        if command == "list":
            core.list_items()
        
        if command == "export":
            core.export_items()
        
        if command == "quit":
            break

def get_inputs():
    while True:
        name = input("item name: ")
        if name:
            break
        print("Invalid input. Please enter a valid item")

    while True:
        store = input("Store name: ")
        if store == "skip":
            store = None
            break
        elif store:
            store = store
            break
        print("Invalid input. Please add a valid store name")

    while True:
        try:
            cost = input("item price: ")
            if cost == "skip":
                cost = None
                break
            else:
                cost = float(cost)
                break
        except ValueError:
            print("Invalid input. Please enter a valid price")

    while True:
        try:
            amount = input("Item quantity: ")
            if amount == "skip":
                amount = None
                break
            elif int(amount) > 0:
                amount = int(amount)
                break
            else:
                print("Quantity must be a positive number")
        except ValueError:
            print("Invalid input. Please enter a valid quantity")

    while True:
        try:
            priority = input("Priority: ")
            if priority == "skip":
                priority = None
                break
            elif 1 <= int(priority) <= 5:
                break
            else:
                print("Priority must be between 1 and 5")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5")

    while True:
        try:
            buy = input("Buy: ")
            if buy.lower() =="true":
                buy = True
                break
            elif buy.lower() == "false":
                buy = False
                break
            elif buy == "skip":
                buy = "skip"
                break
            else:
                print("Invalid input. Please enter true or false")
        except ValueError:
            print("Invalid input. Please enter 'true' or 'false'")

    return name, store, cost, amount, priority, buy

if __name__ == "__main__":
    launch()