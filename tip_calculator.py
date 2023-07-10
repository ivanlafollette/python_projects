myBill = float(input("What was the bill?: $"))
numberOfPeople = int(input("How many people?: "))
billTotal = myBill / numberOfPeople
tip = int(input("How much of a tip percentage will you tip? "))

# Calculate the tip and amount
tipAmount = billTotal * (tip / 100)
totalAmount = billTotal + tipAmount

# formats the answer
formatted_answer1 = f"{billTotal:.2f}"
formatted_answer2 = f"{tipAmount:.2f}"
formatted_answer3 = f"{totalAmount:.2f}"

#final amounts printed
print()
print("OKay, this is what you owe:")
print("--------------------------")
print("Your bill before tip: ", formatted_answer1)
print("Your tip amount: ", formatted_answer2)
print("----------------------------")
print("Your total: ", formatted_answer3)
