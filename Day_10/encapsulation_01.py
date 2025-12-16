# Core Pillars of Object Orientated Programming
'''
Encapulsation is a way of bundling methods inside of a class then
controlling access to the data.
- Protect sensitive data
- Prevent unintended changes
- Control how your data is used
Mark attributes as private; using getters and setters to mark how they are viewed.

- What is public?
- What is private?
'''

class Ramen:
    def __init__(self, broth_type, ingredients):
        self.broth_type = broth_type
        self.__ingredients = ingredients
    
my_ramen = Ramen("Miso", ["Noodles", "Tofu", "Green Onions"])
print(my_ramen.__ingredients)

@property # You can add a getter for a private attribute - allows controlled access
def ingredients(self):
    """Getter for ingredients."""
    return self.__ingredients

@ingredients.setter
def ingredients(self, ingredient):
    """Setter for ingredients with validation."""
    if ingredient.lower() != "strawberries":
        self.__ingredients.append(ingredient)
        print(f"Added {ingredient} to your ramen.")
    else:
        print("Sorry, strawberries don't belong in this ramen.")


my_ramen = Ramen("Miso", ["Noodles", "Tofu", "Green Onions"])
print(my_ramen)

'''
Encapsulation means hiding the details of how something works
and allowing controlled access to it
'''

# Getter Methods - Use the @property decorator to read a private attribute safely
@property
def ingredients(self):
    return self.__ingredients

# Setter Methods - Use the @attribute.setter decorator to control updates
@ingredients.setter
def ingredients(self, ingredient):
    return self.__ingredients


def ingredients(self, ingredient):
    if ingredient.lower() != "strawberries":
        self.__ingredients.append(ingredient)
        print(f"Added {ingredient} to your ramen.")
    else:
        print("Sorry, strawberries don't belong in this ramen.")

# The Ramen Class
class Ramen:
    def __init__(self, broth_type, ingredients):
        self.broth_type = broth_type
        self.__ingredients = ingredients
    
    @property
    def ingredients(self):
        return self.__ingredients
    
    @ingredients.setter
    def ingredients(self, ingredient):
        if ingredient.lower() != "strawberries":
            self.__ingredient.append(ingredient)
            print(f"Added {ingredient} to your ramen.")
        else:
            print("Sorry, strawberries don't belong in this ramen.")
    
my_ramen = Ramen("Miso", ["Noodles", "Tofu", "Green Onions"])
my_ramen.ingredients = "Mushrooms"
my_ramen.ingredients = "Strawberries"

'''
Key Takeways
- Encapsulation protects your data and who can change it
- Use __ to make attributes private in Python
- Use @property and @setter to safely expose and modify private data
- Think your class like a kitchen: let users order the dish, but don;t let them
open the oven
'''

