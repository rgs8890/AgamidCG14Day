# Methods

class CoffeeOrder:
    total_orders = 0

    def __init__(self):
        self.orders = []
        CoffeeOrder.total_orders += 1
    
    def add_order(self, drink):
        if drink not in self.orders:
            self.orders.append(drink)
        else:
            print("Item is already in the order.")

    def cancel_order(self, drink):
        if drink in self.orders:
            self.orders.remove(drink)
            print(f"{drink} removed from your order.")
        else:
            print(f"{drink} not found in your order.")
    
    def show_order(self):
        print("Your order:", ", ".join(self.orders))
    
    # Exercise 1 - Instance Methods
    def clear_orders(self):
        """Clears the entire order list."""
        self.orders = []
        print("Your order has been cleared.")

    @classmethod
    def get_total_orders(cls):
        return cls.total_orders
    
    @staticmethod
    def is_valid_drink(drink):
        return isinstance(drink, str) and bool(drink.strip())
    
my_order = CoffeeOrder()
print(my_order.add_order("Latte"))

print(my_order.cancel_order("Latte"))

print(my_order.show_order())

order1 = CoffeeOrder()
order2 = CoffeeOrder()
order3 = CoffeeOrder()
order4 = CoffeeOrder()
order5 = CoffeeOrder()

print(CoffeeOrder.get_total_orders())

items = ["Capuccino", 7, "Latte"]
for item in items:
    print(CoffeeOrder.is_valid_drink(item))


