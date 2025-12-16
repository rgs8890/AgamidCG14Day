# Inheritance - create a new class from an existing one
# Child Class - subclass which inherits everything from the parent
# A base stays the same but each generation adds their own spin
class Pasta:
    def __init__(self, name, sauce):
        self.name = name
        self.sauce = sauce
    
    def cook(self):
        return f"Cooking {self.name} with {self.sauce} sauce."
    
class Carbonara(Pasta): # These inherit the properties from the Pasta Class
    pass


class PestoPasta(Pasta):
    def __init__(self, name):
        Pasta.__init__(self, name, "Marinara")
    

carbonara = Carbonara("Spaghetti Carbonara", "Creamy Egg and Cheese")
pesto = PestoPasta("Penne Pesto", "basil and garlic")

print(carbonara.cook())
print(pesto.cook())

'''
Inheritance is when one class (a child) automatically gets the attributes 
and methods of another class (the parent)

- Avoid copy-pasting code
- Make changes in one place
- Organise related classes
- Allow for shared behaviours to specific customizations
'''

