my_list = []

while True: 
    list_input = int(input("Add a number into the list. "))
    my_list.append(list_input)

    list_continue = input("Continue to add numbers to the list or find the largest one? Y/N ").lower()
        
    if list_continue == "y":
        continue
    
    elif list_continue == "n": 
        largest = my_list[0]

        for i in range(1, len(my_list)):
            if my_list[i] > largest:
                largest = my_list[i]

        print(largest)
        break



