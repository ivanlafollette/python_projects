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
        
        print("The largest number you entered in the list:", largest)
        
        # LEt's find the location of the number in the list.
        # Note -- the for loop doesn't into account repeated numbers.
        to_find = largest
        found = False
        for i in range(len(my_list)):
             found = my_list[i] == to_find
             if found:
                break
            
        if found:
            print("This is the entire list: ", my_list)
            print("Element found at index", i)
        
        break