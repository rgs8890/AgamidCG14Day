# Top Down Approach Example: Making a Taco

toppings = ["Lettuce", "Cheese", "Salsa"]
quantities = ["1 cup", "1/2 cup", "2 tbsp"]

toppings_with_quantities = zip(toppings, quantities)

for topping, quantity in toppings_with_quantities:
    print(f"{topping}: {quantity}")


def make_taco():
    taco_type = choose_taco()
    ingredients = gather_ingredients()
    assemble_display_taco(taco_type, ingredients)


def choose_taco():
    """Prompt the user for the type of taco they want to make."""
    taco_type = input("What kind of taco are you making? (e.g., Chicken, Beef, Veggie): ")  
    return taco_type


def gather_ingredients():
    """Gather ingredients from the user until they indicate they are done."""
    ingredients = []
    while True:
        ingredient = input("Enter an ingredient (or 'done' to stop):")
        if ingredient.lower() == 'done':
            break
        ingredients.append(ingredient)

    return ingredients


def assemble_display_taco(taco_type, ingredients):
    """Assemble the taco with the given type and ingredients."""
    print(f"\nMaking a {taco_type} taco with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")
    print(f"\nYour {taco_type} taco is ready! Enjoy!")


def add_ingredient(ingredients, ingredient):
    """Add an ingredient to the ingredients list."""
    ingredients.append(ingredient)
    return ingredients


def calculate_cost(ingredients):
    """Calculate the total cost of the ingredients."""
    cost_per_ingredient = 0.5  # Assume each ingredient costs $0.50
    total_cost = len(ingredients) * cost_per_ingredient
    return total_cost


def display_list_cost(ingredients, total_cost):
    """Display the list of ingredients and the total cost."""
    print("\nIngredients List:")
    for ingredient in ingredients:
        formatted_ingredient = format_ingredients(ingredient)
        print(formatted_ingredient)
    print(f"\nTotal Cost: ${total_cost:.2f}")


# Exercise 2: Helper Function
def format_ingredients(ingredient):
    """Format the ingredient string to have each word capitalized."""
    new_ingredient = f"-{ingredient}"
    return new_ingredient

