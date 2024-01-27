question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().casefold()
# Using .strip() to remove extra spaces.

# The HITCHIKERS GUIDE TO THE GALAXY is a classic Douglas Adams book.
# Using match-case is similiar to using if and else.
# I had to research .casefold() since it's like using .lower() if I used if-else.
match question:
    case "42" | "forty two" | "forty-two":
        print("Yes")
    # _ acts as a wildcard.
    case _:
        print("No")