from abc import ABC, abstractmethod

class BakeryItem(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def bake(self):
        return "Baking an item"

class Croissant(BakeryItem):
    def __init__(self, name):
        self.name = name
    
    def bake(self):
        return f"Baking butter layers for {self.name}"

class Muffin(BakeryItem):
    def __init__(self, name):
        self.name = name
    
    def bake(self):
        return f"Baking sweet batter with blueberries for {self.name}"

croissant = Croissant("croissant")
muffin = Muffin("muffin")

bakery_items = [croissant, muffin]

for item in bakery_items:
    print(item.bake())