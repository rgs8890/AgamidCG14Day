"""
    Top 10 Popular Common Standard Libraries

    1. os - Let's you interact with the operating system.
            Makes it easy to handle files, directories and run system commands.
            File-Handling and Directory Management.
    2. sys - Allows you to interact with the runtime environment.
             Provides functions and variables that can be used to manipulate
             the python runtime. Including command line arguments and system
             path settings.
    3. json - Read and write JSON data.
              JSON is a common format for storing and transferring data.
    4. datetime - Used to work with dates and times.
                  Provides classes for manipulating dates, times and durations.
    5. math - Provides mathematical functions like square roots,
              trigonometry and logarithms.
    6. random - Generate random numbers and make random selections.
                Useful for simulations, games and testing.
    7. re - Regular expressions for pattern matching in strings.
             Useful for validating input, searching and text processing.
             Searcd, validate and manipulate text data.
    8. urllib - Work with URLs and handle internet data.
                It allows you to fetch data from the web for scraping or 
                interfacing with online API's
    9. collections - Specialised data structures
                     Like names tuples, and default dictionaries, to help
                     write cleaner and more efficient code.
    10. itertools - Provide functions that create efficient iterators
                     For looping through data in complex ways.
                     Useful for tasks involving combinations, permutations and 
                     creating complex iteration patterns
    11. uuid - Generate unique identifiers
                Useful for creating unique keys for database entries,
                objects and files.
"""
# There are 450,000+ libraries available in Python

import os
import sys
import datetime
import math
import random
import re
import urllib
import collections
import itertools
import uuid
import json

"""
    In other words:
    - os: Operating System interations
    - sys: Python runtime settings
    - json: Working with JSON Data
    - datetime: Dates and Times
    - math: Mathematical Operations
    - random: Random Number Generation
    - re: Pattern Matching with Regular Expressions
    - collections: Advanced Data Structures
    - itertools: Efficient Iterators
"""
# Exercise 1
stores = ["Walmart", "Target", "Costco", "Whole Foods"]

# Why are these libraries popular?
# Pyhton is loved for its simplicity and versatility; to its massive ecosystem
# of libraries. Solve everyday problems from file handling and text manipulation
# to working with numbers and data

# OS - Operating System
print(os.getcwd())
#os.mkdir("new_folder")

# Sys - Python Runtime Settings
print(sys.version)
print(sys.path)

data = '{"name": "apple", "cost": 3.75}'
parsed_data = json.loads(data)
print(parsed_data["name"])

from datetime import datetime
now = datetime.now()
print("Current time:", now)

# Random Library lets you generate random numbers, useful for
# games or simulations
import random
print(random.randint(1, 10))

# re - Pattern Matching with Regular Expressions
import re
text = "my favourite food is fav_food"
result = re.sub("fav_food", "sushi", text)
print(result)

# urllib - Web Requests
from urllib import request
response = request.urlopen("http://example.com")
print(response.read())

# collections - Advanced Data Structures
from collections import Counter
fruits = ["apple", "banana", "apple", "orange"]
print(Counter(fruits))

# iterltools - Efficient Iteration
from itertools import permutations
items = [1, 2, 3]
for perm in permutations(items):
    print(perm)