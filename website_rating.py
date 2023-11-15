
# This Python code creates a dictionary called websiteInfo with keys "name," "url," "description," and "rating," each initially set to None. The code then prompts the user to input relevant values for each key using a for loop that iterates over the keys. The input values are assigned to the corresponding keys in the dictionary.

# After gathering user input, the code prints the entered values for each key in the websiteInfo dictionary using another for loop that iterates over the dictionary's items. The output displays the keys and their associated values.

websiteInfo = {"name": None, "url": None, "description": None, "rating": None}

for name in websiteInfo.keys():
  websiteInfo[name] = input(f"Enter relevant values for {name}: ")

print()
for name, value in websiteInfo.items():
  print(f"{name}: {value}")

# NOTE 1: The .keys() method is used to return a view of all keys in a dictionary.
# NOTE 2: The .items() method returns a view of all key-value pairs in a dictionary as tuples.
