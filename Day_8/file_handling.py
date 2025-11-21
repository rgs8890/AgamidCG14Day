# Writing to files in Python

# Open the file in write mode ('w')
file = open("example.txt", "w")

# Write some text to the file
file.write("This is the first line of text. \n")
file.write("Writing to the file using 'w' mode. \n")

# Close the file to save changes
file.close()

print("File has been written successfulyy.")

lines = [
    "This is the first line of text.\n",
    "This is the second line of text. \n",
    "Writing multiple lines using writelines().\n"
]

with open("example.txt", "w") as file: # Ensures file is closed when it is already done writing
    file.writelines(lines)

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

print(file)


# file.close()

# # Open the file in append mode ('a')
# file = open("example.txt", "a")

# Write new content to the file
with open("example.txt", "a") as file:
    file.write("This is a new line added in append mode.\n")
    file.write("Appending content keeps the existing data intact.\n")


with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# # Close the file to save changes
# file.close()

# print("Contnet has been appended successfully.")




