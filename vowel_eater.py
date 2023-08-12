# Your task here is very special: you must design a vowel eater! Write a program that uses:
# a for loop;
# the concept of conditional execution (if-elif-else)
# the continue statement.
# Your program must:

# ask the user to enter a word;
# use user_word = user_word.upper() to convert the word entered by the user to upper case; we'll talk about string methods and the upper() method very soon – don't worry;
# use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
# print the uneaten letters to the screen, each one of them on a separate line.

print("We're going to ask you for a word, and all the vowels will be eaten. Ok? Great!")
print()

loop = 0
while loop > -1:
    user_word = input("What word do you want? ")
    user_word = user_word.upper()
    if user_word == "":
        print("This is not a word.")
        loop += 1
        continue
    if user_word == "end":
        break
    else:
        # This would be easier placing "A, E, I, O, U" in a variable and using "not in" operator. 
        for j in user_word:
            if j == "A":
                continue
            elif j == "E":
                continue
            elif j == "I":
                continue
            elif j == "O":
                continue
            elif j == "U":
                continue
            else:
                print(j)
        # Break is outside the for loop. 
        break