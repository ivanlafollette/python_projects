# A simple exponents program. 
print("This program will raise a number to the nth degree that you specify.")
print()

# Get the base input as a string
base_input = input("What number do you want as the base? ")

# Check if the input is a digit using string methods -- strip() and isdigit().
if base_input.strip().isdigit():
    # Convert the input to an integer
    base = int(base_input)

    # Get the degree input as a string
    degree_input = input("What is the exponent? ")

    # Check if the degree input is a digit
    if degree_input.strip().isdigit():
        degree = int(degree_input)
        print(base ** degree)
    else:
        print("This isn't a number.")  
else:
    print("This isn't a number.")
       