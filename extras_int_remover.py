# This removes extra numbers from a list.

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

different = []

# This forloop simply says, "if a number isn't in different, place it there."
for i in my_list:
	
    if i not in different:
        different.append(i)

# We make reequate my_list back to the different list. 
my_list = different
print("The list with unique elements only: ")
print(my_list)

