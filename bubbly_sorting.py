# This uses a bubble sorting method.
bubble_list = []
is_swapped = True

# Determines range
user_num = int(input("How many numbers do you want sorted? "))

for i in range(user_num):
    user_val = (input("Enter a number: "))
    bubble_list.append(user_val)

while is_swapped:
    is_swapped = False
    for i in range(len(bubble_list) - 1):
        if bubble_list[i] > bubble_list[i + 1]:
            # performs a swap.
            is_swapped = True
            bubble_list[i], bubble_list[i + 1] = bubble_list[i + 1], bubble_list[i]

print("\nAnd like magic:")
# Removes the number from a list format.
print(", ".join(bubble_list))