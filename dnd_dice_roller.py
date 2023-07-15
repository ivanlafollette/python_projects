# Day 24
# Need this for the randomizer. 
import random

print("-----------------")
print(" DnD Dice Roller ")
print("-----------------")
print()

def diceRoller(desiredDice):
  # Creates the random number plus the number of times being rolled. 
  for i in range (manyTimes):
    myNumber = random.randint(1, desiredDice)
    print("Out of", desiredDice, "you rolled a", myNumber)

while True:
  choices = [4, 6, 8, 10, 12, 20]
  print("What sided dice do you want? It must be D4, D6, D8, D10, D12, or D20.")
  desiredDice = int(input("Number only > "))
  
  if desiredDice not in choices:
        print("Try again. It must be one of the listed sided dice.")
        continue
      
  print("How many times do you want to make this roll? ")
  manyTimes = int(input(" > "))

  diceRoller(desiredDice)
  goAgain = input("Do you want to go again? Y\\N ").lower()
  if goAgain == "y":
    continue
  else:
    print("Bye!")
    break
