dict_a = {"name": "milk"}
dict_a = {"name": "milk", "cost": 6.50, "store": "Save-On", "amount": 2}
print(dict_a)
# These are all keys which are part of the dictionary in key-value pairs
dict_a["cost"] = 5.75
print(dict_a)

dict_a["buy"] = True
print(dict_a)

# Gives the keys and values as pairs
print(dict_a.keys())
print(dict_a.values())
print(dict_a.items()) # Tuples for Key Value
dict_a.pop("amount")
print(dict_a)
dict_a.clear() # Clear the dictionary of all items
print(dict_a)

# Create, Access and Modify Values, Use-Built In Methods
