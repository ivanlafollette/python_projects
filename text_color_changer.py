print("Hey you! Enter a sentence, and I will color it! Give me lots of words! ")
sentence = input(" > ")

# Use the \033[ ANSI escape code to begin the colored section. 

def color_change(sentence):
  for colored in sentence:
    if colored == "r" or colored == "R":
      print('\033[31m', end='') #red
    elif colored == "b" or colored == "B":
      print('\033[34m', end='') #blue
    elif colored == "g" or colored == "G":
      print('\033[32m', end='') #green
    elif colored == "y" or colored == "Y": 
      print('\033[33m', end='') #yellow
    elif colored == "p" or colored == "p": 
      print('\033[35m', end='') #purple
    # Resets the color to white. 
    elif colored == " ":
      print('\033[0m', end='')
    print(colored, end="")

color_change(sentence)
