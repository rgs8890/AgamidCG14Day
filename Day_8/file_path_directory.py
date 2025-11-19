# File Paths and Directories
# Creating new folders
# Checking for new files or navigating directories
import os

# getting the current working directory
current_dir = os.getcwd()

# Listing the directories
dir_list = os.listdir()
for dir in dir_list:
    print(dir)

# Joining directory paths
dir_path = os.path.join(current_dir, "/c/Users/rgs88/OneDrive/Python_14_Day/Day_8")
print(dir_path)

# exists = os.makedirs(dir_path)
# print(exists)

# Printing the current working directory
import os

current_dir = os.getcwd()

print(f"The current working directory is: {current_dir}")

# Listing the contents of a directory
dir_list = os.listdir("/c/Users/rgs88/OneDrive/Python_14_Day/")
for dir in dir_list:
    print(dir)

# Making a new directory
#os.makedirs() # creates nested directories in one command, automatically missing any parent directories
#os.mkdir() # creates a single directory at a specified path; with the parent directories already existing

#os.mkdir("parent_folder/nested_folder")

# Example os.makedirs()
#os.makedirs("parent_folder/nested_folder")

print("Directories 'parent_folder/nested_folder' created!")

# Example: os.mkdir()
import os

#os.mkdir("new_folder")
print("Directory 'new_folder' created!")

# However, if you try a nested directory and parent_folder which does not exist; this will raise an error
#os.mkdir("parent_folder/nested_folder")

# Example: os.makedirs()
#os.makedirs("parent_folder/nested_folder")
print("Directories 'parent_folder/nested_folder' created!")

# Check to see if a file_path exists
file_path = "Day_8"

if os.path.exists(file_path):
    print(f"The file '{file_path}' exists!")
else:
    print(f"The file '{file_path}' does not exist.")

# Building File Paths
# The os.path.join() function is used to combine multiple parts of a file path into a single, valid path. It
# automatically handles the correct path separator (/ or |) based on the operating system, making it platform
# independent

path = os.path.join("test_project", "python", "module8", "test_script.py")
print("Complete Path:", path)

# Removing Files and Directories
# These functions os.remove(), os.rmdir(), shutil.rmtree() - deletes a directory and all its contents 
# (including files and subdirectories)
import os

file_path = "example.txt"

if os.path.exists(file_path):
    os.remove(file_path)
    print(f"File '{file_path}' deleted successfully!")

dir_path = "empty_folder"

if os.path.exists(dir_path):
    os.rmdir(dir_path)
    print(f"Directory {dir_path} deleted successfullty!")
else:
    print(f"Directory '{dir_path}' does not exist.")

# Shutil
import shutil

dir_path = "non_empty_folder"

if os.path.exists(dir_path):
    shutil.rmtree(dir_path)
    print(f"Directory '{dir_path}' and its contents deleted successfully")
else:
    print(f"Directory '{dir_path}' does not exist.")

