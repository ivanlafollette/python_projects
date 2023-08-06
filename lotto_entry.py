# This will create a lotto entry, which will compare the entered number and the list with lotto numbers.
print("You will add six numbers between 1 and 50. We will see how many lotto numbers you get.")

drawn = []
bets = [3, 7, 11, 42, 34, 49]

# A list created to add successfully matched numbers from the user's drawn number list. 
success = []

# The list for the numbers entered by the user. 
lotto_entry = 0

# The total number of successful matches. 
hits = 0

# A variable for the loop of six numbers. 
lotto = 0

while lotto < 7:
    
    lotto_entry = int(input("Enter a lotto number: "))
    drawn.append(lotto_entry)                   
    lotto += 1

    if lotto == 6:
        
    # A for loop that determines if "number" is found in the drawn list.           
        for number in bets:
            if number in drawn:
                
                # For each for loop with a "number in drawm" -- hits gets added with a number. 
                success.append(number)
                hits += 1
                
        # The results are printed. 
        print(success)
        print(hits)
        break
