
# I will need to create the "guessing" section as a function since restarting the game goes back to P1's original word. A slight bug. I will come back to this and re-do!
import os
import time

print("Let's play a two-player word game!")
print("Player one will enter a word. However long it is, player 2 will get that many chances to guess the word.")
print("How about that? OK, let's begin!")

input("Press enter to begin.")
# This is an attempt to avoid an error on Windows systems.
os.system("cls" if os.name == "nt" else "clear")

input("Player 2, go away for a minute so player 1 can take their turn! Hit enter before you do!")
os.system("clear")


def word_game():
    
    p1_word = input("Player 1, enter your word: ").lower()
    print("The word you entered is", p1_word)
    print("Sorry, we have to make it all lower case. Dats how it goes!")
    
    time.sleep(2)
    os.system("cls" if os.name == "nt" else "clear")
    
    #This sets the length of guesses to P1's word. 
    guesses = len(p1_word)
    guess_total = 0
  
    while True:
      
 # This creates underscore blanks for each letter.
      guessed_word = "_" * len(p1_word)
      print("Player 1, you have", guesses, "tries to guess the word.")
      print("The word so far:", guessed_word)
  
      for i in range(guesses):
        
          guess = input("Guess a letter: ").lower()
  
          if guess in guessed_word:
              print("You've tried that letter already!")
              print("The word so far:", guessed_word)
              guess_total += 1
              print("You have guessed", guess_total, "times.")
          #Checks to see if the guessed letter is in P1's word. 
          elif guess in p1_word:
              print("Correct guess!")
              # [idx] = index
              # This shows how the guessed word looks with the correct letters or an underscore. 
            
              guessed_word = "".join([c if c == guess or guessed_word[idx] != "_" else "_" for idx, c in enumerate(p1_word)])
              print("The word so far:", guessed_word)
              guess_total += 1
              print("You have guessed", guess_total, "times.")
          elif guessed_word == p1_word:
            print("Congratulations! Player 1 wins!")
            print("Game over!")
            break
          elif guess not in guessed_word:
              print("Wrong guess!")
              print("The word so far:", guessed_word)
              guess_total += 1
              print("You have guessed", guess_total, "times.")
  
          else:
            print("Player 2 loses!")
            print("Game over!")
            break
    
word_game()
