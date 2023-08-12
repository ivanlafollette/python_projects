# Vowel eater using a "not in" operator:

print("We're going to ask you for a word, and all the vowels will be eaten. Ok? Great!")
print()

loop = 0
while loop > -1:
    user_word = input("What word do you want? ")
    user_word = user_word.upper()
    vowels = "A, E, I, O, U"
    if user_word == "":
        print("This is not a word.")
        loop += 1
        continue
    if user_word == "end":
        break
    else:
        # This would be easier placing "A, E, I, O, U" in a variable and using "not in" operator. 
        for j in user_word:
            if j not in vowels:
                print(j)