from getpass import getpass as input

# Introduction.
print(
    "Hear ye, hear ye! It's time for an PvP epic battle of Rock, Paper, and Sciccors!"
)
print(
    "The rules are that you won't be able to see each others moves as you take them at the keyboard, so choose wisely!"
)
print("Get it? Got it. Good! let's begin!")
print()

# A list, defined within the params, to create the choices that the player can lose.
choices = ["r", "p", "s"]

# This dictionary maps the "choices" into their full form via key-value pairs.
full_choices = {"r": "rock", "p": "paper", "s": "scissors"}

p1Score = 0
p2Score = 0

# The game commences.
print("Alright, with that out of the way, let's begin!")

# Creates a while loop so that the game doesn't end after one round.
while True:

  p1Play = input("Player1, select your move: R, P, or S? ").lower()
  p2Play = input("Player2, select your play: R, P, or S? ").lower()
  print()

  # If the player doesn't choice correctly, they must go again per "not in" and teh "choices" list and the "continue" command.
  if p1Play not in choices or p2Play not in choices:
    print("Invalid choice. Try again.")
    continue

  # Convert the choices to a full forms var. This uses the dictionary key-value pair, which is "full_forms" and [p1Play] or [p2Play] to convert from letters to words.
  p1Play_full = full_choices[p1Play]
  p2Play_full = full_choices[p2Play]

  print("Player1 chose " + p1Play_full)
  print("Player2 chose " + p2Play_full)
  print()

  if p1Play == p2Play:
    print("It's a tie!")
    print()
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes" or play_again.lower() == "y":
      continue
    else:
      exit()

  elif (p1Play == "r" and p2Play == "s"):
    p1Score += 1
    print("Rock smashes scissors! Player 1 wins the game! They have won",  p1Score, "times.")
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes" or play_again.lower() == "y":
      continue
    else:
      exit()

  elif (p1Play == "s" and p2Play == "r"):
    p2Score += 1
    print("Rock smashes scissors! Player 2 wins the game! They have won",  p2Score, "times.")
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes" or play_again.lower() == "y":
      continue
    else:
      exit()

  elif (p1Play == "p" and p2Play == "r"):
    p1Score += 1
    print("Paper covers rock! Player 1 wins the game! They have won",  p1Score, "times.")
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes" or play_again.lower() == "y":
      continue
    else:
      exit()
  elif (p1Play == "r" and p2Play == "p"):
    p2Score += 1
    print("Paper covers rock! Player 2 wins the game! They have won",  p2Score, "times.")
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes" or play_again.lower() == "y":
      continue
    else:
      exit()

  elif (p1Play == "s" and p2Play == "p"):
    p1Score += 1
    print("Scissors cuts paper! Player 1 wins the game! They have won",  p1Score, "times.")
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes" or play_again.lower() == "y":
      continue
    else:
      exit()
  elif (p1Play == "p" and p2Play == "s"):
    p2Score += 1
    print("Scissors cuts paper! Player 2 wins the game! They have won",  p2Score, "times.")
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes" or play_again.lower() == "y":
      continue
    else:
      exit()

print("Bye for now.")