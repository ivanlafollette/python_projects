
# This Python code creates a dictionary called websiteInfo with keys "name," "url," "description," and "rating," each initially set to None. The code then prompts the user to input relevant values for each key using a for loop that iterates over the keys. The input values are assigned to the corresponding keys in the dictionary.

# After gathering user input, the code prints the entered values for each key in the websiteInfo dictionary using another for loop that iterates over the dictionary's items. The output displays the keys and their associated values.

def get_user_input():
  websiteInfo = {"name": None, "url": None, "description": None, "rating": None}

  for name in websiteInfo.keys():
      websiteInfo[name] = input(f"Enter relevant values for {name}: ")

  print()
  for name, value in websiteInfo.items():
      print(f"{name}: {value}")

  return websiteInfo

def main():
  while True:
      websiteInfo = get_user_input()

      startOver = input("\nWould you like to start over? (y/n): ").lower()
      if startOver == "y":
          continue  # Restart the loop
      else:
          print("Thank you for using the program!")
          break  # Exit the loop

if __name__ == "__main__":
  main()
