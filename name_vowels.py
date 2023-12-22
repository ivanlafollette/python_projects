# This defines a function: "names"
# This isn't the most useful program, but I want to reference it later. 
def names():
    # Set up name variable with input
    name = str(input("Please enter your name: "))
    # Create a set of the vowels.
    # Use the intersection() function and the name variable with set().
    if set("aeiou").intersection(name.lower()):
        print("Your name contains a vowel.")
    else:
        print("Your name does not contain a vowel.")

    # Iterate over name.
    # Make the vowels bold.
    for letters in name:
        print(letters)

# Call the function
names()