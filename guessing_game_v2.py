#Imports the random library. 
import random

print("Player 1, the computer, is going to pick a number from 1 to 10. Let's see if you, Player 2, can gues the same number!")

# I tweaked it so that the human player picks the high number. Seems a bit foolhardy since this game can go on for a long time. 
print("Player 2, what is the highest number you want in the guessing range? The higher the harder!")
P2High = int(input("So, what do you want? "))
print()

guessScore = 0

while True:
  
  # Picks a random number from 1 to 10. 
  myNumber = random.randint(1, P2High)

  # If Player 2 chooses a negative number, or a number greater than 10, they lose. 
  if myNumber <= 0 or myNumber > P2High:
    print("That's not allowed! You lose right off the bat, you cheater!")
    break
    
  yourGuess = int(input("Player2: what's your guess? > "))

  guessScore += 1

  if yourGuess <= 0 or yourGuess > P2High:
    print("That's not allowed! You lose right off the bat, you cheater!")
    break
    
  elif yourGuess == myNumber:
    print("Player 1: You chose", myNumber)
    print("Player 2: You choose", yourGuess)
  
    print("Good job, Player 2! You got it right! It took you", guessScore, "times!")
    goAgain = input("Try again? Y/N ").lower()
    if goAgain == "y":
      guessScore = 0
      print("It's a new game! Starting over.")
      continue
       
  elif yourGuess > myNumber:
    print("Player 1: You chose", myNumber)
    print("Player 2: You choose", yourGuess)
   
    goAgain = input("Nope, too high. You lose, Player 2. Try again? Y/N? ").lower()
    if goAgain == "y":
      continue
    else:
      exit()

  elif yourGuess < myNumber:
    print("Player 1: You chose", myNumber)
    print("Player 2: You choose", yourGuess)
    
    goAgain = input("Nope, too low. You lose, Player 2. Try again? Y/N? ").lower()
    if goAgain == "y":
      continue
    else:
      exit()


    
    
    
  