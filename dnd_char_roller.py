# Day 25
# Need this for the radomizer. 
import random

#Begin the program. 
print("---------------------------")
print("  Character Stat Generator ")
print("---------------------------")
print()

charName = input("What is your character's name? ")
charSpecies = input("What is your character species? ")
charClass = input("What is your character class? ")
print()
print("Now, let's roll up some ability scores for", charName)
print()

# Values for the variables at hand. 
strRoll = ""
strDice = 6

#For str
def strRoller(strDice):
  # for i in range (4):
  strRoll1 = random.randint(1, strDice)
  strRoll2 = random.randint(1, strDice)
  strRoll3 = random.randint(1, strDice)
  strRoll4 = random.randint(1, strDice)

  # Check to see which roll is the lowest. Yes, this is a long way of doing it. 
  if strRoll1 < strRoll2 or strRoll1 < strRoll3 or strRoll1 < strRoll4:
    strRoll = strRoll2 + strRoll3 + strRoll4
    print("Your strength is", strRoll)
    return strRoll

  if strRoll2 < strRoll1 or strRoll2 < strRoll3 or strRoll2 < strRoll4:
    strRoll = strRoll1 + strRoll3 + strRoll4
    print("Your strength is", strRoll)
    return strRoll

  if strRoll3 < strRoll1 or strRoll3 < strRoll2 or strRoll3 < strRoll4:
    strRoll = strRoll1 + strRoll2 + strRoll4
    print("Your strength is", strRoll)
    return strRoll

  if strRoll4 < strRoll1 or strRoll4 < strRoll2 or strRoll4 < strRoll3:
    strRoll = strRoll1 + strRoll2 + strRoll3
    print("Your strength is", strRoll)
    return strRoll


# Calls the strRoller(strRoll) subroutine. 
strRoll = strRoller(strDice)
# print("Your strength is", strRoll)


# subroutine has parameter called `number`
# number` shows how many numbers we want the pin to have
#def pinPicker(number):
# import random
  #this is the empty string
#  pin = "" 
  #for loop shows defined amount of random numbers
 # for i in range(number): 
    #we want a string of random numbers between 0-9
 #   pin += str(random.randint(0,9)) 
    
 # return pin
  
#4 means we want 4 random numbers
#myPin = pinPicker(4) 
#print(myPin)