# Write to a file that is read-only
# Exception-Handling and Permissions: Permisisons are managed by the file system

# File Permissions - chmod
# Who can read/write or execute?

# Three types
# Read(r) - view contents
# Write (w) - modify or delete the file
# Execute (e) -  run the file as a program/script

# Three Types
# Read(r) - list contents
# Write(w) - add, modify or delete
# Execute(e) - navigate into the directory

# When the user account shouldn't have access to write permissions for the file
import os

file_path = "example.txt"

try:
    with open(file_path, "r") as file:
        file.write("Attempting to write a file without proper permissions. \n")
    print("File written successfully")
except PermissionError:
    print(f"PermissionError: You do not have access to #{file_path}")

    ## chmod +w example.txt

# Try-Except for file operations
# File permissions (rwx)
# Managing permissions
# Using with open for safety
# 