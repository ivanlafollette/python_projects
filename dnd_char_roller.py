# Day 25
# Need this for the randomizer. 
import random

#Begin the program. 
print("---------------------------")
print("  Character Stat Generator ")
print("---------------------------")
print()

char_name = input("What is your character's name? ")
char_species = input("What is your character species? ")
char_class = input("What is your character class? ")
print()
print("Now, let's roll up some ability scores for", char_name)
print()

# Values for the variables at hand. 
str_roll = ""
str_dice = 6

#For str
def str_roller(str_dice):
  # for i in range (4):
  str_roll1 = random.randint(1, str_dice)
  str_roll2 = random.randint(1, str_dice)
  str_roll3 = random.randint(1, str_dice)
  str_roll4 = random.randint(1, str_dice)

  # Check to see which roll is the lowest. Yes, this is a long way of doing it. 
  if str_roll1 < str_roll2 or str_roll1 < str_roll3 or str_roll1 < str_roll4:
    str_roll = str_roll2 + str_roll3 + str_roll4
    print("Your strength is", str_roll)
    return str_roll
          
  if str_roll2 < str_roll1 or str_roll2 < str_roll3 or str_roll2 < str_roll4:
    str_roll = str_roll1 + str_roll3 + str_roll4
    print("Your strength is", str_roll)
    return str_roll

  if str_roll3 < str_roll1 or strRoll3 < str_roll2 or strRoll3 < str_roll4:
    str_roll = str_roll1 + str_roll2 + str_roll4
    print("Your strength is", str_roll)
    return str_roll

  if str_roll4 < str_roll1 or str_roll4 < str_roll2 or str_roll4 < str_roll3:
    str_roll = str_roll1 + str_roll2 + str_roll3
    print("Your strength is", str_roll)
    return str_roll


# Calls the strRoller(str_roll) subroutine. 
str_roll = str_roller(strDice)
print("Your strength is", str_roll)

# subroutine has parameter called `number`
# number` shows how many numbers we want the pin to have
#def pin_picker(number):
# import random
  #this is the empty string
#  pin = "" 
  #for loop shows defined amount of random numbers
 # for i in range(number): 
    #we want a string of random numbers between 0-9
 #   pin += str(random.randint(0,9)) 
    
 # return pin
  
#4 means we want 4 random numbers
#myPin = pin_picker(4) 
#print(my_pin)
