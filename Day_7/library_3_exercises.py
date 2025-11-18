# Exercise 1
import re
receipt = "Apples: $2.99, Banaas: $1.50, Milk: $3.75, Eggs: $4.20"

pattern = r"\$\d+\.\d{2}"

print(re.findall(pattern, receipt))

# Exercise 2
grocery_list = [
    "some bread",
    "A Can of Diced Tomatoes",
    "A can of peas",
    "An Heirloom Tomato",
    "1 beefsteak tomato",
    "A Block of Cheese",
    "3 tomatoes on the vine"
]
pattern = r".*\b(tomato|tomatoes)\b.*"

for item in grocery_list:
    if re.search(pattern, item, re.IGNORECASE):
        print(item)

# Exercise 3
grocery_list = [
    {"name": "milk", "store": "Walmart"},
    {"name": "bread", "store": "Walmart"},
    {"name": "eggs", "store": "Walmart"},
    {"name": "peanut butter", "store": "Costco"},
    {"name": "chicken", "store": "Costco"}
]

pattern_2 = r".*\b(peanut butter)\b.*"
for item in grocery_list:
    if re.search(pattern_2, item["name"], re.IGNORECASE):
        print(item)

# Exercise 4: Removing units from a Shoppin List: re.sub()
grocery_list3 = [
    "2kg apples",
    "5lbs potatoes",
    "3g salt",
    "1kg bananas",
    "250g rice"
]

pattern3 = r"\d+\s?(kg|lbs|g)?"
# for item in grocery_list:
#     if re.search(pattern3, item, re.IGNORECASE):
#         print(item)
new_items = []
for item in grocery_list3:
    cleaned = re.sub(pattern3, "", item).strip()
    new_items.append(cleaned)

print(new_items)