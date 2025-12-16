class TacoStand:
    def __init__(self, name, tacos, daily_special):
        self.name = name
        self.__tacos = tacos
        self.__daily_special = daily_special
    
    @property
    def tacos(self):
        '''Getter for tacos'''
        return self.__tacos
    
    @tacos.setter
    def tacos(self, taco): # Python only allows one parameter for this
        '''Only allows valid taco ingredients to be added.'''
        acceptable_tacos = ["beef", "chicken", "lettuce", "cheese", "salsa"]
        if taco.lower() in acceptable_tacos:
            self.__tacos.append(taco)
            print(f"Added {taco} to the taco stand!")
        else:
            print("Sorry, this is not the type of taco we want in the Taco Stand.")
    
    @property
    def daily_special(self):
        return self.__daily_special
    
    def update_special(self, new_special, role):
        '''Only allows the chef to update the daily special.'''
        if role.lower() == "chef":
            self.__daily_special = new_special
            print(f"Daily special updated to: {new_special}")
        else:
            print("Only the chef can update the daily special!")

    @daily_special.setter
    def daily_special(self, new_special):
        self.__daily_special = new_special
    
# Exercise 3 - Test it
taco_stand = TacoStand("my_stand", ["beef", "cheese"])

taco_stand.tacos = "lettuce"
taco_stand.tacos = "chocolate"

print(taco_stand.tacos)

my_stand = TacoStand("Skyler's Tacos", ["beef", "cheese"], "Chicken & Salsa")
print(my_stand.daily_special)
my_stand.update_special("Carnitas Supreme", role = "chef")
my_stand.update_special("PB&J", role = "customer")
print(my_stand.daily_special)

# Use custom methods when the logic needs more than one input or extra behaviour


