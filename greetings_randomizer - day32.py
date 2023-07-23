# Import random function. 
import random 

# The list with the languages. 
greetings = ["Hola!", "Bonjour!", "Salve", "Goddag", "Gutentag"]

# This randomizes an index. 
index = random.randint(0,4)

# This prints via a "f" statement and then attaches the randomizer index variable to the greetings list. 
print(f"This is a random greeting: {greetings[index]}")

# The loop print from the greetings list. 
for i in greetings:
  print("This is from a loop: ", i)
 