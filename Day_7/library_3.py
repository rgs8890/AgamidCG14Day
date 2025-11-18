# REGEX - Regular Expressions 
# Programming in general with regular expressions
# Find, Validate and Manipulate Text: Sequence of characters

# allows you to find text that has concise patterns
# saves a lot of time

# Whenever you want to find validate and match text with a new pattern
# Text Searching 
# Text Replacement

# Data Extraction
# Getting names, dates from a document

# re -> allows for pattern matching in strings with expressions
import re
# re.match()
# re.search()
# re.findall()
# re.sub()

# Searches for the first occurrence of a pattern anywhere in a string
# Replace all given addresses in a given text

text = "Contact us at info@example.com or support@example.org."
pattern = r'\b[A-Za-z0-9._%+-]+@'

emails = re.findall(pattern, text)
print(emails)


import re

text = "apples, bananas, carrots"
pattern = r"^apples"

result = re.match(pattern, text)
if result:
    print("The list starts with apples!")
else:
    print("No match.")


text2 = "I need eggs, milk, and bread."
pattern2 = r"milk"

result2 = re.search(text2, pattern2)
if result2:
    print("Milk found:", result.group())
else:
    print("Milk not found.")

# re.findall() will find all occurrences of a pattern and returns them as a list
import re

receipt = "Apples: $2.50, Bananas: $1.20, Bread: $3.75"
pattern = r"\$\d+\.\d{2}"

prices = re.findall(pattern, receipt)
print("Prices:", prices)

# re.sub() replaces all parts of the string that match the pattern with
import re

text = "apples, bananas, milk, bread"
new_text = re.sub(r", ", "\n", text)
print("Shopping list:\n", new_text)
# Regex is a powerful tool when working with text data

match = re.search(r"(\d+)\s(apples)", "I bought 10 apples.")
print(match.group(0))
print(match.group(1))
print(match.group(2))