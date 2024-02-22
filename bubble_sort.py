# A bubble sort
my_list = [4, 5, 3, 1, 2]  
swapped = True 
 
while swapped:
    swapped = False
    # This iterates over the list, stopping one element short of the end (since it compares element i with i + 1).
    for i in range(len(my_list) - 1):
        
        if my_list[i] > my_list[i + 1]:
            swapped = True 
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
 
print(my_list)