# Escape Sequences and Special Characters
# Escape Sequences are special combinations of characters
print("Item\t\tPrice")
print("Coffee\t\t$2.50")
print("Sandwich\t\t$5.00") # Including tabs

# \'
print("It\'s everyone\'s birthday")
# \n \t \\ \r
# 
print("I hate tennis \n Sanjay is gay")

# \\
print("Today's special: Chef's famous pasta \\ Alfredo Sauce.")

# \r - Carriage Return
print("Today's special: Pizza\rPasta")

formatted_text = "Menu:\n\nItem\t\tPrice\nCoffee"

with open("menu.txt", "w") as file:
    file.write(formatted_text)

print("The formatted menu has been written to 'menu.txt'.")

# What escape sequence are and why they are needed?
# Excape Sequences and Special Characters are essential components of Python that
# allow you to represent characters in strings that might otherwise be difficult to include
# Enable formatting of strings, including non-printable characters, or use symbols

file_path_x = "C:\\Users\\John\\Documents\\menu.txt"
print(file_path_x)