# import sys
# print("PYTHON USED:", sys.executable)

import os
import datetime
import pandas as pd
import numpy as np
import math


from math import sqrt

# Using math.sqrt to calculate
square_root = math.sqrt(16)

# Using sqrt to calculate the square root
square_root = sqrt(16)
print(square_root)
# Aliases
# Reading Documentation -> An instruction manual 
# Available FUnctions -> Required Parameters, Examples of how to use them

# There are two types of libraries
# Standard Librareis -> Bundled with Python and ready-to-use
# Third-Party Libraries -> Created by developers worldwide, hosted on Pypi
# Examples include: NumPy, Pandas, Flask

# Benefits of Libraries
# Efficiency: Reuse pre-written code for faster development
# Readbility: Built on tested solutions, making programs more robust

def get_square_root(number):
    """
    Calculate and print the square root of a given number.
    Args: 

    Args:
        number (float or int): The number to calculate the square  root of
    Returns:
        None: This function prints the result directly.
    """
    square_root = math.sqrt(number)
    print(f"The square root of {number} is {square_root}")

number = 64
get_square_root(number)