from random import randint

#This will create a list of play options.
t = ["Rock", "Paper", "Scissors"]

#This assigns a random play to the computer
computer = t[randint(0,2)]

#Sets player to False
player = False

while player == False:
#set player to True
    player = input("Pick your poison: Rock, Paper, Scissors? ").lower()
    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "Paper":
            print("You lose! Haha, sucker!", computer, "covers", player)
        else:
            print("You win! Cheater!", player, "smashes", computer)
    elif player == "paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    elif player == "Exit":
        print("Bye for now!")
        break
    else:
        print("Negative. Check your spelling!")
        
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]
