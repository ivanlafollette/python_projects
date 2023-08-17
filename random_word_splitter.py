# This program will input a sentence, and choose a random word from it. 

# Import random() library
import random

# picks a random item from a list.
# random.choice() 

sentence = input("Input a sentence, and I will choose random words from it: ")

# Use the split() function to split the sentence into a list. 
list_of_words = sentence.split()
# Adds blue color to the text.
print("This list that is created:", '\033[34m', list_of_words)

chosen_words = random.choice(list_of_words)
# Adds red color to the text.
print("\033[0mA random word:",'\033[31m', chosen_words)