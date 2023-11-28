print("I will convert English into pig latin!")
print()
userWords = input("What is your word? ").lower()
converted = userWords[1:]
converted2 = userWords[0]
print(f"Here is your pig latin: {converted}{converted2}ay")
