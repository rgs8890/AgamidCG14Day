# Reading from a File
# Handle reading efficiently - Reading data from files
file = open("example.txt", "r")

content = file.read()

print("File Content:")
print(content)

#with open("example.txt", "r") as file:
file.close()

print("Reading lines one by one:")
#line = file.readline() # Read the first line
# while line: # Loop until there are no more lines
#     print(line.strip()) # Print the line
#     line = file.readline() # Read the next line

file.close()

# Opening a file in "r" mode
# read() get the file as one string
# readline() one file at a time
# readlines() all lines in one list

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# Writing Multiple Lines with writelines()
file = open("example.txt", "w")

lines = [
    "First Line\n",
    "Second Line\n",
    "Third Line\n"
]

file.writelines(lines)

file.close()

with open("example.txt", "r") as file:
    for line in file:
        print(line)
     

# with open("example.txt", "r") as file:
#     for line in file:
#         print(line.strip())

# Opening a File in Read Mode - Before reading from a file, it must be opened in read mode (r)
file = open("example.txt", "r")

# Understanding File Permissions
'''
 :p Read (r) allows viewing the file content
 :p Write (w) allows modifying or deleting the file
 :p Execute (x) allows running the file as a program
 
 :Read allows listing files in the directory
 :Write allows creating or deleting files in the directory
 :Execute allows navigating into the directory

 Owner is the user who owns the file
 Group of users who have specific permissions
 Others are all other users
'''

try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
except PermissionError as pe:
    print("Error: You do not have the necessary permissions.")