# Exercise 1:
import os

current_dir = os.getcwd()

print(current_dir)

# Exercise 2: Dynamically construct paths and create directories
new_path = os.path.join(current_dir, "/Project/Module1/Data.")
# os.makedirs(new_path)

# # Exercise 3: Make a file in the directory
data_file = os.path.join(current_dir, "/Project/Module1/Data./data.txt")
# os.makedirs(data_file)

data_file2 = os.path.join(current_dir,  "/Project/Module1/Data./data2.txt")
# os.makedirs(data_file2)

# Exercise 4
directories = os.listdir(new_path)

for dir in directories:
    print(dir)

# Exercise 5
# if os.path.exists(new_path):
#     os.remove(data_file2)
#     print(f"File '{data_file2} deleted successfully!")
# else:
#     print(f"File '{data_file2}' does not exist.")

import shutil
shutil.rmtree(new_path)