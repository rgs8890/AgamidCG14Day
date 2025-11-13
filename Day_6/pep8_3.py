# Why Documenting my Code Matters?
# Inline Comments

# Initialise base value for calculations
value = 5

# Docstrings -> provide context, functions, classes or modules.
def add_numbers(x, y):
    """
    Adds two numbers.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The sum of x and y.
    """

    return x + y

# Exercise 1: Inline Comments
def spearate_fruits_and_veggies(items):
    '''
    Seperates a list into two lists of fruits and vegetables

    Args:
        items (list): List of items to be separated

    Returns:
        fruits (list): List of fruits
        veggies (list): List of vegetables
    '''
    # Declare empty list for fruits
    fruits = []
    # Declare empty list for vegetables
    veggies = []

    # Loop through each item in the list
    for item in items:
        # Assign name, category to the tuple in the list 
        name, category = item
        # Check if category is fruit and append to list
        if category == "fruit":
            fruits.append('name')
        else:
            veggies.append(name)
    
    # Returns two lists, one of fruits, the other of vegetables
    return fruits, veggies
