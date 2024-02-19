hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
print("Here is a list of nunmbers: ", hat_list)
print()
# Step 1: write a line of code that prompts the user
replace_int = int(input("What numbers shall replace the middle number? "))
# to replace the middle number with an integer number entered by the user.

hat_list[2] = replace_int
print(hat_list)

# Step 2: write a line of code that removes the last element from the list.

del hat_list[-1]

# Step 3: write a line of code that prints the length of the existing list.
print(len(hat_list))

print(hat_list)

