import math
from datetime import date

print(date.today())

def welcome():
    return "Welcome to this Math Module"

# Basic operations
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

# Power and roots
def power(a, b):
    return math.pow(a, b)

def square_root(a):
    if a < 0:
        return "Error: Cannot take square root of a negative number."
    return math.sqrt(a)

# Trigonometric functions
def sine(x):
    return math.sin(x)

def cosine(x):
    return math.cos(x)

def tangent(x):
    return math.tan(x)

# Rounding and absolute value
def absolute_value(a):
    return abs(a)

def round_number(a, decimals=0):
    return round(a, decimals)

# Logarithms
def natural_log(x):
    if x <= 0:
        return "Error: log undefined for non-positive values."
    return math.log(x)

def log_base(x, base):
    if x <= 0 or base <= 0:
        return "Error: log undefined for non-positive values."
    return math.log(x, base)