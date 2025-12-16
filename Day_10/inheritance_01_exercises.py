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
        Pasta.__init__(self, name, "Pesto")

class AlfredoPasta(Pasta):
    pass

class MarinaraPasta(Pasta):
    def __init__(self, name):
        Pasta.__init__(self, name, "Marinara")

alfredo = AlfredoPasta("Penne", "Alfredo")
print(alfredo.cook())

class Dessert:
    def __init__(self, name):
        self.name = name

class Gelato(Dessert):
    def serve(self):
        return f"Serving a cold bowl of {self.name} gelato!"

dessert = Gelato("Strawberry")
print(dessert.serve())