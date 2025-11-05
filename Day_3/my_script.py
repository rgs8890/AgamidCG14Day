# Lists and Tuples
my_list = [1, 2, "apple", 4.5, "tomato", 75]
a_list = ["these", "are", "elements"]
# Start counting at 0
get_item = my_list[2]
print(get_item)

# Slicing
first_three = my_list[0:3]
print(first_three)

# my_list[start:stop:step]
# Start is where it begins, Slice is where it ends (does not print this value)
my_list_x = [0,1,2,3,4,5]
print(my_list_x[1:4])
print(my_list_x[:3])
print(my_list_x[2:])

# The default step is 1
print(my_list[0:5:3])

# Negative Indices
print(my_list_x[-3]) # starts at the last index which is -1 then counts back -2 then 3 (-3)

# Positive Index counts forward from 0, Negative Indexing counts backward from -1
print(my_list[::-1])

#Ommitting the start or stop includes everything before and after
# Built in methods
my_shopping_list = ["bread", "milk", "eggs"]
my_shopping_list.append("banana")
my_shopping_list.remove("milk")
print(my_shopping_list)

my_shopping_list.sort()
print(my_shopping_list) #an argument is a value or a variable that is passed into a function or method when it is called; whereas a parameter is a constraint in a function

my_shopping_list.sort(reverse=True) # () indicates this is a method
#.extend() adds an element from another list
my_shopping_list.extend(["spinach", "cucumber"])
print(my_shopping_list)

#.insert
my_shopping_list.insert(1, "oil")
print(my_shopping_list)

#.pop(), .index(), .count(), .reverse(), .clear()

# Tuples are immutable
my_tuple = (10, 20, 30)
print(my_tuple[0])
print(my_tuple[0:2]) # There are less built-in methods then lists
list_a = [1,2]
list_b = [3,4]
tuple_a = [1,2]
tuple_b = [3,4]
print(list_a + tuple_b)

#Things which do not change
#Lists are flexible, they let your add, remove, and change data
#Tuples are great for locking in data
