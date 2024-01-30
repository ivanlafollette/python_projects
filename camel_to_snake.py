def main():

    # User input.
    camel = input("camelCase: ").strip()

    # Prints the converted text using the came_snake function.
    print("snake_case: ", camel_snake(camel))

def camel_snake(camel_s):

# This function will complete the conversion.
# This empty var is needed to store the converted text.
    snake_s = ""

    # Iterates through the inputted argument from camel via camel_s.
    for i in camel_s:
        # Asks if i finds upper letters.
        if i.isupper() and i != 0:
            # Adds an underscore when the upper is found.
            snake_s += "_"
        # And then converts the upper to lower.
        snake_s += i.lower()

    # Returns the var with the converted text.
    return snake_s

main()

