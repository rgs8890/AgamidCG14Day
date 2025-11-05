# Sets are useful for storing collections os unique items, like unique user names, product codes, and then perform quick comparisons within collections

# Practice Exercises 1
fruits = {'apple', 'banana', 'cherry'}
fruits.add('orange')
fruits.remove('banana')
print(fruits)

# Practices Exercises 2
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
intersection_set = set_a.intersection(set_b)
print(intersection_set)
union_set = set_a.union(set_b)
print(union_set)

# Practice Exercises 3
set_x = {'cat', 'dog', 'fish'}
set_y = {'dog', 'bird'}
diff_set = set_x.difference(set_y)
print(diff_set)

