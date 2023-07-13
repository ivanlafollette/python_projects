
from random import randint

# This is the starting position
position = (("-", "-", "-"),("-", "-", "-"),("-","-","-"))

computer_wins = "The computer wins!"
human_wins = "The human wins!"
tie = "It's a tie!"

computer_player = "O"
human_player = "X"

whoseMove = ""

empty = "-"

def map(n, f):
    
    ret = []
    
    for i in range(0, len(n)):
        ret.append(f(n[i]))
    return ret

def computer_assign(position, move, computer_player):
    
    return position[:move[0]] + (position[move[0]][:move[1]] + (computer_player,) + position[move[0]][move[1]+1:],) + position[move[0]+1:]

def human_assign(position, move, human_player):

# Move check

    return position[:move[0]] + (position[move[0]][:move[1]] + (human_player,) + position[move[0]][move[1]+1:],) + position[move[0]+1:]

def generateMoves(position):

    i = 0
    j = 0
    
    moves = []

    for i in range(3):
        for j in range(3):
            if position[i][j] == "-":
                moves.append((i, j))
                          
    return moves

def computerMove(position):
    
    openMoves = generateMoves(position)

    index = randint(0, len(openMoves) - 1)

    move = openMoves[index]

    position = computer_assign(position, move, computer_player)

    global whoseMove
    whoseMove = computer_player

    print("It's the computer's move.")
    print(" -------------")
    
    for x in position:

        print(" |", x[0], "|", x[1], "|", x[2], "|", "\n", "-------------")

    # This would print out the board as tuples.
    """for x in position:

        print(x)"""
   
    detect_result(position)

def humanMove(position):

    print(" ")
    print("It's the human's move.")

    move = tuple(map(input("Enter your move as two numbers separated by a space: ").split(), int))
    print(" -------------")

    position = human_assign(position, move, human_player)

    global whoseMove
    whoseMove = human_player

    for y in position:
        print(" |", y[0], "|", y[1], "|", y[2], "|", "\n", "-------------")

    # This would print out the board as tuples.
    """for y in position:

        print(y)"""

    print(" ")
    
    detect_result(position)

def detect_result(position):
    
    def hum_winsRow(position, human_player):
        
        for i in range(0, 3):
            if position[i][0] == human_player and position[i][1] == human_player and position[i][2] == human_player:
                return True
        return False
    
    def com_winsRow(position, computer_player):
        
        for j in range(0, 3):
            if position[j][0] == computer_player and position[j][1] == computer_player and position[j][2] == computer_player:
                return True
        return False

    def hum_winsColumn(position, human_player):
        
        for i in range(0, 3):
            if position[0][i] == human_player and position[1][i] == human_player and position[2][i] == human_player:
                return True
        return False

    def com_winsColumn(position, computer_player):
        
        for j in range(0, 3):
            if position[0][j] == computer_player and position[1][j] == computer_player and position[2][j] == computer_player:
                return True
        return False                                                                                                                       
    
    def hum_winsDiagonal(position, human_player):
        
        if position[0][0] == human_player and position[1][1] == human_player and position[2][2] == human_player:
            return True
        elif position[0][2] == human_player and position[1][1] == human_player and position[2][0] == human_player:
            return True
        else:
            return False

    def com_winsDiagonal(position, computer_player):
        
        if position[0][0] == computer_player and position[1][1] == computer_player and position[2][2] == computer_player:
            return True
        elif position[0][2] == computer_player and position[1][1] == computer_player and position[2][0] == computer_player:
            return True
        else:
            return False
                                                                                                                            
    def tieGame(position):
        
        for i in range (0,3):
            for j in range(0,3):
                if position[i][j] == empty:
                    return False
        return True
    
    if com_winsRow(position, computer_player) or com_winsColumn(position, computer_player) or com_winsDiagonal(position, computer_player):

        print(computer_wins)
    
    elif hum_winsRow(position, human_player) or hum_winsColumn(position, human_player) or hum_winsDiagonal(position, human_player):
        
        print(human_wins)
    
    elif tieGame(position):

        print(tie)
    
    else:
      
        if whoseMove == "O":
            humanMove(position)
       
        elif whoseMove == "X":
            computerMove(position)
      
computerMove(position)

