from abc import ABC, abstractmethod

class Coffee(ABC):
    def __init__(self, name):
        self.name = name
    
    def prepare_espresso(self):
        return f"Brewing a strong espresso shot for {self.name}"

    @abstractmethod
    def prepare_milk(self):
        pass

    def serve(self):
        return f"Serving {self.name} in a cup."

class Latte(Coffee):
    def prepare_milk(self):
        return f"Streaming milk and adding it to {self.name}"
    
class Capuccino(Coffee):
    def prepare_milk(self):
        return f"Frothing milk for a creamy {self.name}"

class Mocha(Coffee):
    def prepare_milk(self):
        return f"Mixing steamed milk with chocolate for {self.name}"

class FlatWhite(Coffee):
    def prepare_milk(self):
        return f"Steaming milk with microfoam for a silky {self.name}"

latte = Latte("latte")
flatwhite = FlatWhite("flat white")
mocha = Mocha("mocha")

coffees = [latte, flatwhite, mocha]

for coffee in coffees:
    print(coffee.prepare_espresso())
    print(coffee.prepare_milk())
    print(coffee.serve())

#coffee = Coffee("coffee")
# TypeError