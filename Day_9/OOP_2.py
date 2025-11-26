'''
Classes and Objects

:p How do you build it?
:p What can it do?

An object is a product of the class. Each clone it creates is an object.

'''
class Human:
    def __init__(self, name, iq):
        self.name = name
        self.iq = iq
    
    def introduce(self):
        if self.iq < 69:
            print(f"Me {self.name}. Me find rock. Me smash rock. Rock make fire.")
        else:
            print(f"Hi, I'm {self.name}, I am a bi-pedal carbon based lifeform.")

original_human = Human("Bob", 100)
clone_1 = Human("Jeff", 140)
clone_2 = Human("Grog", 28)

# original_human = Human(name, iq)
original_human = Human("Bob", 100)

print(original_human.introduce())
print(clone_2.introduce())



'''
Each object is independent, each object is also unique.
Grouping attributes keeps clone cleaned and organised.
A class is like a blueprint that can describe how something is built and what it can do.
An object is a specific copy created from that blueprint.

- Classes are blueprints that define how objects are built and what they can do.
- Objects are specific instances created from a class.
- __init__ is a setup for a project
'''

