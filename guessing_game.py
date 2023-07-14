from getpass import getpass as input

print("Player 1 is going to pick a number from 1 to 10. Let's see how many times it takes for player 2 to get it right!")

guessScore = 0

while True:

  myNumber = int(input("Player1: Let me put in a number: > "))

  if myNumber <= 0 or myNumber > 10:
    print("That's not allowed! You lose right off the bat, you cheater!")
    break
    
  yourGuess = int(input("Player2: what's your guess? > "))

  guessScore += 1

  if yourGuess <= 0 or yourGuess > 10:
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


    
    
    
  