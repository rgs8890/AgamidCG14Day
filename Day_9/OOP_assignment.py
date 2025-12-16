# Exercise 1 - Classes
class BaseCharacter:
    character_count = 0

    def __init__(self, name, height, weight):
        self._name = name
        self.height = height
        self.weight = weight
        BaseCharacter.character_count += 1
    
    @classmethod
    def get_character_count(cls):
        return cls.character_count

    @property
    def name(self):
        ''' Getter for name '''
        return self._name
    
    @name.setter
    def name(self, value):
        '''Setter for name'''
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value



# Exercise 2 - Instances
character_a = BaseCharacter("Little Billy", 150, 110)

print(f"{character_a.name} is {character_a.height} cm tall and {character_a.weight} lbs.")

# Exercise 3 - Class Attributes/ Variables and Class Methods
print(f"Characters created: {BaseCharacter.get_character_count()}")

# Exercise 4 - Getters and Setters
# character_a.name = 7

character_a.name = "Riley"
print(f"The name of character A is {character_a.name}")

# Exercise 5 - Inheritance
class Orc(BaseCharacter):
    def __init__(self, name, height, weight):
        super().__init__(name, height, weight)
        self.horns = None
        self.weapon = None
        self.war_cry = None
    
    @staticmethod
    def creation_logger(func):
        def wrapper(self, *args, **kwargs):
            print("Creating character...")
            print("==============")
            result = func(self, *args, **kwargs)
            print("==============")
            print("Character complete.")
            return result
        
        return wrapper
    
    @BaseCharacter.creation_logger
    def generate_description(self):
        description_parts = [
            (
                f"{self.name} is a towering orc, standing {self.height} cm tall "
                f"and weighing {self.weight} lbs."
            )
        ]

        if self.horns:
            description_parts.append(f"They have intimidating {self.horns} horns.")

        if self.weapon:
            description_parts.append(
                f"Known for their fierce combat prowess, they wield a fearsome {self.weapon}, "
                "daunting to any enemy that lives to see it."
            )

        if self.war_cry:
            description_parts.append(
                "You know you're in trouble if you hear the rumbles of the horrid "
                "war cry that accompanies every battle: "
                f"{self.war_cry}!"
            )

        description = " ".join(description_parts)
        print(description)

    

character_b = Orc("Grommash", 210, 240)
print(f"{character_b.name} is {character_b.height} cm tall and {character_b.weight} lbs.")

print(f"Characters created: {BaseCharacter.get_character_count()}")

character_b.generate_description()

# Exercise 8
class PoisonDartFrog(BaseCharacter):
    number_of_frogs = 0
    number_of_killer_frogs = 0
        
    def __init__(self, name, height, weight):
        super().__init__(name, height, weight)
        self.poison = 1000
        self.jump = 10
        self.color = None
        self.victims = []
        self.top_killer = False
        PoisonDartFrog.number_of_frogs += 1
    
    @classmethod
    def get_frogs(cls):
        return PoisonDartFrog.number_of_frogs
    
    def exercise_bootcamp(self):
        self.poison += 10
        self.jump += 1
        print("Poison Dart Frog's poison has increased by 10 and its jump has increased by 1!")
    
    def attack(self, victim):
        self.victims.append(victim)
        print(f"{self.name} attacked {victim} with {self.poison}")

    def top_killer(self):
        if len(self.victims) >= 10:
            self.top_killer = True
        PoisonDartFrog.number_of_killer_frogs += 1
    
    @classmethod
    def get_top_killer_frogs(cls):
        return PoisonDartFrog.number_of_killer_frogs

    @staticmethod
    def creating_poison_dart_frog(func):
        def wrapper(self, *args, **kwargs):
            print("Creating character...")
            print("===============")
            result = func(self, *args, **kwargs)
            print("===============")
            print("Character complete.")
            return result
    
        return wrapper

    @BaseCharacter.creating_poison_dart_frog
    def generate_description(self):

        description_parts = [
                                (f"You have created a poison dart frog with the name {self.name}"
                                f"and then {self.height} lbs.")
                            ]
        
        





    @BaseCharacter.creation_logger
    def generate_description(self):
        description_parts = [
            (
                f"{self.name} is a towering orc, standing {self.height} cm tall "
                f"and weighing {self.weight} lbs."
            )
        ]

        if self.horns:
            description_parts.append(f"They have intimidating {self.horns} horns.")

        if self.weapon:
            description_parts.append(
                f"Known for their fierce combat prowess, they wield a fearsome {self.weapon}, "
                "daunting to any enemy that lives to see it."
            )

        if self.war_cry:
            description_parts.append(
                "You know you're in trouble if you hear the rumbles of the horrid "
                "war cry that accompanies every battle: "
                f"{self.war_cry}!"
            )

        description = " ".join(description_parts)
        print(description)