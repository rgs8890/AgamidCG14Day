# Lists are when you need flexibility
# Tuples are when you need a fixed unchanging collection

'''
Lists Practice Exercises
'''

# Exercise 1
movies = ["Inception", "Avatar", "Matrix", "Toy Story", "The GodFather"]
print(movies)
movies.append("Batman: The Dark Knight")
movies.append("Inception")
print(movies)

# Exercise 2
numbers = [10, 20, 30, 40, 50]
print(numbers[3:])

# Exercise 3
colors = ['red', 'blue', 'green']
print(colors)
colors.insert(1, 'yellow') #inserts before the given index
colors.insert(len(colors), 'purple') # Use len when inserting at the end of a list
print(colors)

'''
Tuples Practice Exercises
'''

# Exercise 1
dimensions = (10, 5, 15)
print(dimensions[1])
print(dimensions[len(dimensions)//2])

# Exercise 2
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8)
print(numbers[2:6])

# Exercise 3
fruits = ('apple', 'banana')
vegetables = ('carrot', 'lettuce')
groceries = fruits + vegetables
print(groceries)