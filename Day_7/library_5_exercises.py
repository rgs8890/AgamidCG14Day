# What are third-party packages?
'''
Pre-Built tools created by developers outside of the official Python Library
Libraries and Packages can be used interchangeable to cause confusion.

Library -> umbrella term for any collection of reusable code.

A library can be a:
- single module (Requests)
- structured package (Flask, Pandas)

Package refers to organisation of the code. A package
- Is a directory containing one or more Python Modules?
- Includes the __init__.py file to signal a package
- Can itself be part of a larger library

pip -> default Python's package installer -> making it easy to
download, install, upgrade, or uninstall third-party packages

Python Package Index (PyPI)
'''

# Commands
# pip install, 
# pip install --upgrade
# pip uninstall
# pip list


import matplotlib.pyplot as plt
#print("Matplotlib version:", plt.__version__)

# Storing data as two separate lists
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

prices = [
    5.50, 5.45, 5.60, 5.80, 6.00, 6.10,
    6.20, 6.50, 6.70, 6.90, 7.10, 7.20
]

plt.plot(months, prices, marker='o', linestyle = '-', color = 'b')
plt.title("Cost of Olive Oil Over the Last Year")
plt.xlabel("Month")
plt.ylabel("Price ($/L)")
plt.grid(True)

# Display the final plot
plt.show()