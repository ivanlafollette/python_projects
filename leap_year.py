# This program determines a leap year or common year. 

year = int(input("Enter a year: "))

if year < 1582:
    print("That year does not fall within the Gregorian calendar period.")

elif (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    print(year, "is a leap year.")

else:
    print(year, "is a common year.")
