user_num = int(input("How many numbers to sort? "))
# Empty list
my_list = []

# Iterates over the length from the user. 
for i in range(user_num):
    user_val = input("What numbers do you want sorted? ")
    # Appends value to the empty list.
    my_list.append(user_val)

my_list.sort()
print("\nSorted:")
# Removes the number from a list format.
print(", ".join(my_list))