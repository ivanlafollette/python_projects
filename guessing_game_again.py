import random

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

print("I am picking a number between one and ten.")
guess = int(input("What is your guess for my secret number?: "))

secret_number = "0"

while guess != secret_number:
    secret_number = random.randint(1, 11)
    if guess != secret_number:
        print("You're wrong! I picked", secret_number)
        print("Guess again!")
        
    guess = int(input("What is your guess for my secret number? "))

print("I picked", secret_number)
print("You cheater! You got it right!")
