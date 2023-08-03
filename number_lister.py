list = []

while True:
    
    menu = input("Do you want to insert, remove, add, del, or see the list or the length? I, R, A, D, S, L: ").lower()
    
    # The append() method adds the value to the end of the list. 
    if menu == "i":
        value1 = int(input("What value do you want to enter? "))
        list.append(value1)
        
    # The remove() method will remove or delete a value.
    elif menu == "r":
        value2 = int(input("What value do you want to remove? "))
        list.remove(value2)
    
    # This will calculate the total combined values in the list. 
    elif menu == "a":
     
        total = 0
        # Cyclles through . . 
        for i in range(len(list)):
        # Adds the list value, starting from 0, each time the for loop cycles through.
        
            total += list[i]
            
        # And prints the combined value. Important -- keep the print outside the "for" loop. 
        print(total)
    
    # Uses the delete, or del function to delete a value from a position in the list.
    elif menu == "d":
        value3 = int(input("What position in the list do you want to delete? It starts with [0] "))
        del list[value3]           
        
    # Prints tht number of values in the list. 
    elif menu == "l":
        print("List length:", len(list))
        
      # Prints the list.
    elif menu == "s":
        print(list)





