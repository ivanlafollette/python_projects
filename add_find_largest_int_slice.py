my_list = []

while True: 
    list_input = int(input("Add a number into the list. "))
    my_list.append(list_input)

    list_continue = input("Continue to add numbers to the list or find the largest one? Y/N ").lower()
        
    if list_continue == "y":
        continue
    
    elif list_continue == "n": 
        largest = my_list[0]

# This comparison uses a slice instead to find the largest int in the list. 
        for i in my_list[1:]:
            if i > largest:
                largest = i

        print(largest)
        break