# This program will ask for a first and last name, and then print them out together.
# We use two separate lists for each part of the name. 
first_names = []
last_names = []
# We use a list of lists for both first-last names. 
combined_names = [first_names, last_names]

def names_function():
    # The for loop iterates through combined_names. 
    # Prints out the combined first and last names.
    # We use the zip() function to iterate through the lists simultaneously and then concatenates the elements. 
    for first, last in zip(first_names, last_names):
        print(first + " " + last)
    print()

while True:
    f_name = input("What is your first name? ").capitalize()
    first_names.append(f_name)
    l_name = input("What is your last name? ").capitalize()
    last_names.append(l_name)

    names_function()
