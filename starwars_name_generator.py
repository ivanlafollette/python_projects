import time 
print("In a galaxy far far away...")
time.sleep(3)
print()
print("+----------------------------+")
print(" The Star Wars Name Generator")
print("+----------------------------+")
print()

print("Tell me your name, young Jedi, and I will create your Star Wars name.")
sw_first = input("What is your first name? ")
sw_last = input("What is your last name? ")
sw_maiden = input("What is your mother's Maiden name? ")
sw_city = input("What city were you born? ")
# We want to slice from the front, [0:3] and from the end, [4:]
print("Your Star Wars Jedi name is", (sw_first[0:3] + sw_last[-3:]).title() + " " + (sw_maiden[0:3] + sw_city[-3:]).title())