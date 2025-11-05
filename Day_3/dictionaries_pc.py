# Dictionaries are useful for storing data which can be accessible by a specific label or identifier, 
# like a contact list, where each person's name is a key and their details are values
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
values_as_list = list(my_dict.values())
print(values_as_list)

# Practice Exercise 1
book = {'title': '1984', 'author': 'George Orwell', 'year': 1949}
print(book["author"])

# Practice Exercise 2
profile = {}
profile["name"] = "Alice"
profile["age"] = 30
profile["city"] = "paris"
print(profile)

# Practice Exercise 3
student = {'name': 'Emma', 'grade': 'A', 'subject': 'Math'}
print(student)
student.pop('subject')
print(student)
student_details = list(student)
print(student_details)

