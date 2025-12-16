'''
What is abstraction?
- abstraction hides how something works, only to show what it does
- use abstract classes (ABCs) to define structure that child classes follow
- keeps large programs clean, conssitent, and easy to maintain
'''
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

latte = Latte("Latte")
print(latte.prepare_espresso())
print(latte.prepare_milk())
print(latte.serve())

'''
Cannot instantiate an abstract class

Final Pillar of OOP programming - also Super
Abstraction hides the unnecessary details and
forces structure in large programs, it also
defines easy to use interfaces. Abstraction is the
process of hiding implementation details while
enabling essential features. It allows definition of
a general structure,

Encapulsation -> hides how something works and allowing
controlled access to it.

Abstraction -> Hides what is done, like implementation details,
abstract base classes , class that cannot be instantiated,
serves as a blueprint for other classes. Grind beans, brew espresso.

Abstraction simplifies usage and encapsulation is for security and proper
data handling.
'''

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
        return f"mixing steamed milk with chocolate for {self.name}"

latte = Latte("Dulce de latte")
capuccino = Capuccino("Classic Capuccino")
mocha = Mocha("Chocolate Mocha")

print(latte.prepare_espresso())
print(latte.prepare_milk())
print(latte.serve())

print(capuccino.prepare_espresso())
print(capuccino.prepare_milk())
print(capuccino.serve())
