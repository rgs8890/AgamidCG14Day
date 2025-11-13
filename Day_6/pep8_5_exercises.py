grocery_list = {"bread": 4.50, "cheese": 12.47, "yoghurt": 3.99}


#LBYL
if "butter" in grocery_list:
    print(f"Butter: {grocery_list['butter']} units")
else:
    print("Error: Butter is not in the grocery list.")

#EAFP
try:
    print(f"Butter: {grocery_list['butter']} units")
except KeyError:
    print("Error: Butter is not in the grocery list.")