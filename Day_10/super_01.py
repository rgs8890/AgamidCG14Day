'''
Super 
- call methods from a parent class
- reuse inherited behaviour
- extend or modify behaviour

super is a built-in function that allows a child class to 
call methods from its parent class

Super is used for multiple inheritance -> support METHOD_RESOLUTION ORDER

'''
class Tea:
    def __init__(self, name, steep_time, base_ingredient = "tea_leaves"):
        self.name = name
        self.steep_time = steep_time
        self.base_ingredient = base_ingredient
    
    def prepare(self):
        return f"Boiling water and steeping {self.name} for {self.steep_time} minutes."

class GreenTea(Tea):
    def prepare(self):
        super().prepare()
        return f"Gently brewing {self.name} at a lower temperature for {self.steep_time} minutes."

class ChaiTea(Tea):
    def __init__(self, name, steep_time):
        super().__init__(name, steep_time, base_ingredient="tea leaves and spices")

    def prepare(self):
        super().prepare()
        return ( 
            f"Boiling {self.name} with spcies and milk for {self.steep_time} minutes."
        )

chai = ChaiTea("Masala Chai", 5)
print(chai.base_ingredient)

'''
It ensures that the parent class attributes are properly intialized

- reuse methods from the parent class while adding new behaviour
- initialise the parent_class (__init__())
- modify inherited methods

- the child class completely changes a method
'''

