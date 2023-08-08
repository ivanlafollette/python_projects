# We create an empty list.
rolodex = []

# The subroutine to print the list. 
def print_list():
  print()
  # This will iterate over every element in the list. 
  for name in rolodex:
    print(name)
  print()
  #I wanted to see how the list looks for each element. 
  # print(rolodex)
  print()

# The infinite loop. 
while True:
  # We strip spaces when prompted to avoid duplicates and so that the first index is a letter. 
  # We also make sure the name is capitalized. 
  first_name = input("First Name: ").strip().capitalize()
  last_name = input("Last Name: ").strip().capitalize()
  # An elegant solution of using the f-string to create a string with the f-l variables.
  name = f"{first_name} {last_name}"
  # if - not in avoids duplicates. 
  if name not in rolodex:
    rolodex.append(name)
  # Prints this warning if a duplicate is attempted.
  else:
    print("ERROR: Duplicate name")
  # Calls the function. 
  printList()