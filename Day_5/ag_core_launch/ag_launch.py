import ag_core

def launch():
    while True:
        command = input("Enter a command (add, remove, edit, list, export, quit): ")

        if command == 'add':
            name, store, cost, amount, priority, buy = get_inputs()
            ag_core.add_item(name = name, store = store, cost = cost, amount = amount, priority=priority, buy = buy)
        
        if command == 'edit':
            name, store, cost, amount, priority, buy = get_inputs()
            ag_core.edit_item(name, store, cost, amount, priority, buy)
        
        if command == 'remove':
            ag_core.remove(name)
        
        if command == 'export':
            ag_core.export_items()

        
        if command == "list":
            ag_core.list_items()
        
        if command == "quit":
            break

def get_inputs():
    while True:
        name = input("item name: ")
        if name:
            break
        print("Invalid Input. Please enter a valid item.")
    
    while True:
        store = input("Store Name: ")
        if store:
            break
        print("Invalid Input. Please add a valid store name.")
    
    while True:
        try:
            cost = float(input("item price: "))
            break
        except ValueError:
            print("Invalid Input. Please enter a valid price.")
    
    while True:
        try:
            amount = int(input("Item Quantity: "))
            if amount > 0:
                break
            else:
                print("Quantity must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid quantity.")
        
    while True:
        try:
            priority = int(input("Priority: "))
            if 1 <= priority <= 5:
                break
            else:
                print("Priority must be between 1 and 5.")
        except ValueError:
            print("Invalid Input. Please enter a number between 1 and 5.")
    
    while True:
        try:
            buy = input("Buy: ")
            if buy.lower() == "true":
                buy = True
                break
            elif buy.lower() == "false":
                buy = False
                break
            else:
                print("Invalid Input. Please enter true or false.")
        except ValueError:
            print("Invalid Input. Please enter 'true' or 'false'")
    
    return name, store, cost, amount, priority, buy


# If priority is greater than or equal to 1 and less than or equal to 5

if __name__ == "__main__":
    launch()
