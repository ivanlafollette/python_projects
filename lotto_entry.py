# This will create a lotto entry, which will compare the entered number and the list with lotto numbers.
print("You will add six numbers between 1 and 50. We will see how many lotto numbers you get.")
drawn = []
bets = [3, 7, 11, 42, 34, 49]
success = []
lotto_entry = 0
hits = 0
lotto = 0

while lotto < 7:
    
    lotto_entry = int(input("Enter a lotto number: "))
    drawn.append(lotto_entry)                   
    lotto += 1

    if lotto == 6:
                    
        for number in bets:
            if number in drawn:
                success.append(number)
                hits += 1
        
        print(success)
        print(hits)
        break