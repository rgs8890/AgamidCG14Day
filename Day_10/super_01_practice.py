'''
OOP - Object Orientated Programming
Abstraction: Highlights to details and also shows what is needed

- forces structure in large programs
- defines clear and easy-to-use interfaces

Abstracts stuff and only shows some of the picture

Hiding the details of how something works and allowing controlled access
to it.

Abstraction hides implementation details while exposing only essential
features.

A class that cannot be instantiated.


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
        return f"Mixing streamed milk with chocolate for {self.name}"

'''
Rules
- Abstraction hides complexity and structure
- Abstract classes define blueprints but cannot be instantiated
- Subclasses must implement abstract methods
- Abstraction makes code scaleable and maintainable
'''
