# Annotations and Type hints -> helps us see the data types for functions and variables
# Improve readability, and reuse area
# Type Hints are only available in new python versions (3.5+)

def add_numbers(a: int, b: int) -> int:
    return a + b

name: str = "Alice"
age: int = 30
# Type hints are optional; they are not enforced at runtime
# Bonus -> not requirement

# Function Annotations
# Define what types of inputs and outputs there are for functions
def add(x: int, y: int) -> int:
    return x + y

# Function Annotation vs Type Hints
# When we are throwing around terms like type hints and function annotations,
# their definitions and usage can sound the same
# : or -> is any metadata attaches to a functions parameters or return value

# # Function Annotations Example
# def save_file(file_path: "Must be a valid file path" ) -> "Returns True if file saved successfully":
#     # Function implementation
#     return True


# def convert_temperature(temp: "Celsius value", target_unit: "Fahrenheit or Kelvin") -> "Converted temperature":
#     return temp * 9/5 + 32 if target_unit == "Fahrenheit" else temp + 273.15

# Variable Type Hints
name: str = "Alice"
age: int = 30
is_active: bool = True

# Complex Type Hints
grocery_list: List[Dict[str, Union[float, int, str, bool]]]
from typing import List, Dict, Union