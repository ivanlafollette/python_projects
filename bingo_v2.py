import random
import time  # Slows the game's pace down.

# Function to generate a Bingo card
def generate_bingo_card():
    numbers = list(range(1, 26))
    random.shuffle(numbers)
    return [numbers[i:i + 5] for i in range(0, 25, 5)]

# Function to print the Bingo card
def print_bingo_card(card):
    print("-" * 23)
    for row in card:
        print(' | '.join(f"{num:2}" for num in row))
        print("-" * 23)

# Function to draw a number that hasn't been drawn before
def draw_number(drawn_numbers):
    return random.choice([num for num in range(1, 26) if num not in drawn_numbers])

# Function to mark the drawn number on the card
def mark_number(card, number):
    for row in card:
        if number in row:
            row[row.index(number)] = 0

# Function to check if the card has Bingo
def check_bingo(card):
    # Check rows, columns, and diagonals for Bingo
    for i in range(5):
        if all(row[i] == 0 for row in card) or all(num == 0 for num in card[i]):
            return True
    if all(card[i][i] == 0 for i in range(5)) or all(card[i][4-i] == 0 for i in range(5)):
        return True
    return False

# Main function to play the Bingo game
def play_bingo():
    card = generate_bingo_card()
    drawn_numbers = set()
    print("Let's play some bingo!\n")
    print_bingo_card(card)

    while True:
        num = draw_number(drawn_numbers)
        drawn_numbers.add(num)
        print(f"Number drawn: {num}")
        mark_number(card, num)
        print_bingo_card(card)

        if check_bingo(card):
            print("Bingo!")
            break

        time.sleep(5)  # Pause for 5 seconds between rounds

# I need to add a section asking the player if they want to go another round. 

play_bingo()
