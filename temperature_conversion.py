print("Enter a number, and I will convert it from Fahrenheit to celsius, or vice-versa.")

while True:
    
    cel_or_far = (input("Enter 1 if you want from F-to-C or enter 2 if you want from C-to-F: "))
    
    if cel_or_far.isdigit():
        
        cel_or_far = int(cel_or_far)

        if cel_or_far == 1:
            far_cel = round(float(input("Enter the F number you want convert: ")))
            output1 = round((far_cel - 32) * (5 / 9))
            print(f"{far_cel}F is equal to {output1}C.")

        elif cel_or_far == 2:
            cel_far = round(float(input("Enter the C number you want convert: ")))
            output2 = round(cel_far * (9 / 5) + 32)
            print(f"{cel_far}C is equal to {output2}F.")
            
        else:
            print("You didn't enter 1 or 2. Try again.")
    else:
        print("Invalid input. Please enter a number.")
    
    

    