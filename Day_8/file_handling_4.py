# Skyler Fines

# Serialization and JSON
# JSON and DUMP

# Serialization of converting Python Complex Objects -> a format that can be easily saved -> turning data into a portable and sharable format.
# It is key for saving program data to files so that it can be reloaded later

# It can also be used to send data to APIs or storing it in databases
# Pickle -> Complex Objects -> Serializable

# YAML -> requires an external library
# Verbose -> harder to use
# JSON -> human-readable, supported in every language, perfect for web development and data storage
# Python Objects -> JSON is serialization
# JSON -> Python is Deserialization (Decoding)

import json

grocery_list = {"fruits": ["apples", "bananas"], "dairy": ["milk"]}

with open("grocery_list.json", "w") as file:
    json.dump(grocery_list, file)

with open("grocery_list.json", "r") as file:
    loaded_grocery_list = json.loads(file)

# Types in python are different to JSON

'''
Python          | JSON
dict              JSON Object
list/tuple        JSON Array
string            JSON String
int/float         JSON Number
None              JSON null
'''
# JSON -> JavaScript Object Notation