# Serialization is the process of converting a data structure or object into a format that can be easily stored or transmitted and later reconstructed
# It is responsible for sending data over a network, or persisting the state of objects for later use

# Why is serialization important for file handling?
import json

# Serialize (Convert Data to JSON)
data = {"name": "Alice", "age": 25, "is_student": True}
json_string = json.dumps(data)

with open("data.json", "w") as file:
    json.dump(data, file)

# data = json.loads(json_string)

with open("data.json", "r") as file:
    data = json.loads(file)

'''
Serialization/ Deserialization: Concerned with converting to/from JSON format for storage or transmission.
Encoding/Decoding: Focuses on transforming Python objects into JSON strings (encoding) and vice versa (decoding)
'''

