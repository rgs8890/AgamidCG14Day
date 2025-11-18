# Practice Exercises

# 1: Shopping Trip - Itertools
import itertools
stores = ["Walmart", "Costco", "Target", "Whole Foods"]

permutation_list = []
from itertools import permutations
for perm in permutations(stores):
    permutation_list.append(perm)
    print(perm)

print(f"Total possible trips: {len(permutation_list)}")

# Exercise 2: Counting Items in a Shopping Cart
# Counting Items in a Shopping Cart - Collections
shopping_cart = [
    "apple", "banana", "apple", "orange", "banana", "apple",
    "milk", "bread", "milk", "eggs", "bread", "bread",
    "carrot", "carrot", "apple", "orange", "banana", "eggs"
]

from collections import Counter

num_items = Counter(shopping_cart)
print(num_items)

# Exercise 3: Choosing a Restaurant - Random
restaurants = [
    "Pizza Palace",
    "Sushi Spot",
    "Taco Town",
    "Burger Barn",
    "Pasta Paradise",
    "Salad Stop"
]

print(restaurants)

import random
def choose_restaurant(restaurants):
    restaurant = random.choice(restaurants)
    print(f"Tonight's restaurant choice is: {restaurant}")

choose_restaurant(restaurants)

