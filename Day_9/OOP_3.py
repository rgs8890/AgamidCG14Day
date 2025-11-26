'''
__init__ method contains attributes unique to each object. It is a setup process for an object
Python calls __init__ to give it properties/attributes unique to the object
__init__ -> takes two pieces of information
self -> Specific Object being created
Attributes -> store information that makes each object unique

'''
class Human:
    def __init__(self, name, iq, height, weight):
        self.name = name
        self.iq = iq
        self.height = height
        self.weight = weight
    
    def introduce(self):
        if self.iq < 69:
            print(f"Me {self.name}. Me find rock. Me smash rock. Rock make fire.")
        else:
            print(f"Hi, I'm {self.name}, I am a bi-pedal carbon based lifeform.")
    
original_human = Human("Bob", 130, 175, 79)
clone_1 = Human("Ram", 125, 175, 70)

print(f"Height: {original_human.height} cm")
print(f"Weight: {original_human.weight} lbs")

print(original_human.__dict__)
print(vars(clone_1))

# clone_3 = Human("Chad")

# Setting attributes in a Human Class
# clone_3.iq = 130
# clone_3.height = 198
# clone_3.weight = 210
# clone_3.hair_color = "blonde"
# clone_3.eye_color = "blue"
# clone_3.clothing = "high end Kiton Business Suit"

# Exercise
# __init__ is a special method used to set up the object's initial state
class Human:
    def __init__(self, name, iq=None, height=None, weight=None, hair_color=None, eye_color=None, clothing=None, emotion=None, environment=None, special_feature=None):
        self.name = name
        self.iq = iq
        self.height = height # in cm
        self.weight = weight # in lbs
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.clothing = clothing
        self.emotion = emotion
        self.environment = environment
        self.special_feature = special_feature
    
    def introduce(self):
        if self.iq < 69:
            print(f"Me {self.name}. Me find rock. Me smash rock. Rock made fire.")
        else:
            print(f"Hi, I'm {self.name}, I am a bi-pedal carbon-based lifeform.")
    
    def prompt(self):
        return f"""
        Create a highly detailed portrait of a character named {self.name}, 
        who is {self.height} cm tall and weighs {self.weight} lbs. They have 
        an IQ of {self.iq}, reflecting their intelligence and charisma in their 
        demeanor. {self.name} has {self.hair_color} hair, {self.eye_color} eyes, 
        and wears {self.clothing}. Their expression shows {self.emotion}, and 
        they are in a {self.environment}. Highlight their {self.special_feature}.
        """

        
# original_human = Human("Rohit", 140, 175, 180)
# clone_1 = Human("Jeff", 140, 182, 160)
# clone_2 = Human("Grog", 50, 160, 200)
# original_human.name = "Bob"
# original_human.iq = 140
# print(original_human.name, original_human.iq)
# print(clone_1.height)
# print(clone_1.weight)

# print(clone_1.__dict__)
# print(vars(clone_1))

clone_3 = Human("Chad")
clone_3.iq = 130
clone_3.height = 198
clone_3.weight = 210
clone_3.hair_color = "blonde"
clone_3.eye_color = "blue"
clone_3.clothing = "high end Kiton business suit"
clone_3.emotion = "cheeky smirk with raised eyebrows"
clone_3.environment = "business finance office"
clone_3.special_feature = "defined jawline"

print(clone_3.prompt())
# Streamhandlers contorl how log messages appear on the terminal