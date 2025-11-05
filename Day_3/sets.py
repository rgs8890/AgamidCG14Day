a_set = {"these", "are", "elements"}
print(a_set) # However these only hold unique values
a_set.add("noodles")
print(a_set)

# Unless it is already there
a_set.discard("banana")
print(a_set)

my_set = {"apple", "chocolate", "kombucha", "banana"}
my_set.discard("banana")
print(my_set)

# Union combines two sets and gives you all unique elements from both
set_1 = {"cheese", "bread", "deli meat"}
set_2 = {"milk", "eggs", "bread"}
union_set = set_1.union(set_2)
print(union_set)

# Intersection -> Things which are in both sets
set_1 = {"cheese", "bread", "deli meat"}
set_2 = {"milk", "eggs", "bread"}
inter_set = set_1.intersection(set_2)
print(inter_set)

# Difference
diff_set = set_1.difference(set_2)
print(diff_set)

#Removing items
my_set_z = {"apple", "banana", "cherry"}
my_set_z.remove("apple") # Raises an error if the item is not found
my_set_z.remove("banana") # Doest not raise an error if the item is not found