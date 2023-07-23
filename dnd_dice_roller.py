# Day 24
# Need this for the randomizer. 
import random

print("-----------------")
print(" DnD Dice Roller ")
print("-----------------")
print()

def dice_roller(desired_dice):
  # Creates the random number plus the number of times being rolled. 
  for i in range (manyTimes):
    my_number = random.randint(1, desired_dice)
    print("Out of", desired_dice, "you rolled a", my_number)

while True:
  choices = [4, 6, 8, 10, 12, 20]
  print("What sided dice do you want? It must be D4, D6, D8, D10, D12, or D20.")
  desired_dice = int(input("Number only > "))
  
  if desired_dice not in choices:
        print("Try again. It must be one of the listed sided dice.")
        continue
      
  print("How many times do you want to make this roll? ")
  manyTimes = int(input(" > "))

  dice_roller(desired_dice)
  go_again = input("Do you want to go again? Y\\N ").lower()
  if go_again == "y":
    continue
  else:
    print("Bye!")
    break
