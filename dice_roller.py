import random

print("This program will roll a 1d6, or six-sided die.")
begin = input("Hit 'y' to roll! ").lower()
print()
if begin == "y":
    diceroll = random.randint(1,6)
    
    if diceroll == 1:
        print("You rolled a 1!")
        print("===========")
        print("|         |")       
        print("|    O    |")
        print("|         |")
        print("===========")
    
    elif diceroll == 2:
        print("You rolled a 2!")
        print("===========")
        print("|         |")       
        print("| O     O |")
        print("|         |")
        print("===========")
    
    elif diceroll == 3:
        print("You rolled a 3!")
        print("===========")
        print("|    O    |")       
        print("|    O    |")
        print("|    O    |")
        print("===========")
    
    elif diceroll == 4:
        print("You rolled a 4!")
        print("===========")
        print("| O     O |")       
        print("|         |")
        print("| O     O |")
        print("===========")
    
    elif diceroll == 5:
        print("You rolled a 5!")
        print("===========")
        print("| O     O |")       
        print("|    O    |")
        print("| O     O |")
        print("===========")
              
    elif diceroll == 6:
        print("You rolled a 6!")
        print("===========")
        print("| O     O |")       
        print("| O     O |")
        print("| O     O |")
        print("===========")
        
else:
    print("OK, fine, be that way.")    