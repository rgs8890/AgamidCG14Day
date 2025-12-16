# Polymorphism is a way 
# fly()
# FlyingPig, Crane, Sparrow, Woodpecker
# Boil -> Prepare -> Serve
# Polymorphism is a way to use the same function or method for different people each behaving in its own way
# Cleaner, more reusable code
# Different objects same interface
# More flexibility and scalability
class Ramen:
    def __init__(self, name):
        self.name = name
    
    def prepare(self):
        return f"Preparing a bowl of {self.name} ramen."

class TonkotsuRamen(Ramen):
    def prepare(self):
        return f"Simmering pork bones for hours to make {self.name}."

class ShoyuRamen(Ramen):
    def prepare(self):
        return f"Mixing soy sauce base to prepare {self.name}."

class MisoRamen(Ramen):
    def prepare(self):
        return f"Blending miso paste for a flavorful {self.name} ramen."

ramen_types = [TonkotsuRamen("Tonkotsu"), ShoyuRamen("Shoyu"), MisoRamen("Miso")]

for ramen in ramen_types:
    print(ramen.prepare())


# Day 10: Polymorphism: Polymorphism lets different classes share 
# the same method name, but define their own behvaiour

'''
Why use polymorphism?
1. Avoid writing multiple method names for similar tasks.
2. Interact with different objects in a consistent way.
3. Add flexibility without breaking existing code.
'''
class Ramen:
    def __init__(self, name):
        self.name = name
    
    def prepare(self):
        return f"Preparing a bowl of {self.name} ramen."

class TonkotsuRamen(Ramen):
    def prepare(self):
        return f"Simmering pork bones for hours to make {self.name}"
    
class ShoyuRamen(Ramen):
    def prepare(self):
        return f"Mixing soy sauce base to prepare {self.name}"

class MisoRamen(Ramen):
    def prepare(self):
        return f"Blending miso paste for flavorful {self.name}"

ramen_types = [TonkotsuRamen("Tonkotsu"), ShoyuRamen("Shoyu"), MisoRamen("Miso")]

for ramen in ramen_types:
    print(ramen.prepare())


