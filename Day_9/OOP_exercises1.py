'''
Methods: What are methods?
- Methods are functions that live inside a class and define how an object behaves. They are "actions" which your objects can perform.

:P Instance Methods: Act on one specific object
:P Class Methods: Act on the class as a whole
:P Static Methods: Don't act on either. They're just handy tools.

Methods help organise and group code that belongs to the same object or class, making code:
- Easier to read
- Easier to maintain
- Easier to reuse
'''

class CoffeeOrder:
    total_orders = 0

    def __init__(self):
        self.orders = []
    
    def add_order(self, drink):
        self.orders.append(drink)
        print(f"{drink} added to your order.")

    def clear_orders(self):
        """Clears the entire order list."""
        self.orders = []
        print("Your order has been cleared")
    
    def cancel_order(self, drink):
        if drink in self.orders:
            self.orders.remove(drink)
            print(f"{drink} removed from your order.")
        else:
            print(f"{drink} not found in your order")
    
    def show_order(self):
        print("Your order:", ", ".join(self.orders))

    @classmethod
    def get_total_orders(cls):
        return cls.total_orders

    @staticmethod 
    def is_valid_drink(drink):
        return isinstance(drink, str) and bool(drink.strip())

my_order = CoffeeOrder()
my_order.add_order("latte")
my_order.cancel_order("Latte")

print(my_order.show_order())


