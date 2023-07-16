print("+-----------------+")
print("+  Infinity Dice  +")
print("+-----------------+")

print("How many sides do you want on your dice?")
diceSides = int(input("Enter a number > "))

def diceRoller(diceSides):
    import random
    roll = random.randint(1, diceSides)
    print("You rolled a", roll)
        
diceRoller(diceSides)
    
