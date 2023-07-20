
# The arguments in the function (a, b) refers to the first, and second part of the variables when they are called. 

def new_print(a, b):
  
  if a == "red":
    print("\033[31m", b, sep="", end="")
  elif a == "green":
    print("\033[32m", b, sep="", end="")
  elif a == "blue":
    print("\033[34m", b, sep="", end="")
  # I threw in doggy just to prove that the "a" argument could be any word. 
  elif a == "doggy":
    print("\033[35m", b, sep="", end="")
  else:
    print("\033[0m", b, sep="", end="")
    
print("Super Subroutine!")
print()
print("With my ", end="")
new_print("red", "new program")
new_print("reset", " I can just call red ('and') ")
new_print("red", "it will print in red ")
new_print("blue", "or even blue ")
new_print("doggy", "somewhere in the text.")