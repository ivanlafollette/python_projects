"""
This module will calculate the number of seconds per minute, day, month, and year.
"""

print("Tell me a year and I will extrapolate the number of seconds per year.")
print()
yearVAR = int(input("What year do you want to know about? "))
print()

# The calculation for the seconds per minute.
secondsVar = 60
minutesVar = 60
secsMinute = 60 * 60
print("The number of seconds per minute:", secsMinute)
print()

# The calculation for the seconds per hour.
secsHour = secsMinute * 60
print("The number of seconds per hour:", secsHour)
print()

# And the seconds per day.
dayHours = 24
secsDay = secsHour * 24
print("The number of seconds per day:", secsDay )

# Now, using the seconds per day for the month.
secsMonth = secsDay * 31
print()
print("The seconds per month:", secsMonth)

print()

# Calculate if a year is a leap year. Is it divisible by 4 or 100 or 400? if so, run the following code.
if (yearVAR % 4 == 0 and yearVAR % 100 != 0) or yearVAR % 400 == 0:
  leapYear = 366 * secsMonth
  print("This is a leap year so it has 366 days in it. The number of seconds per year is", leapYear)
  
# If not, then run the following code. 
else:
  nonLeapYear = 365 * secsMonth
  print("This is a non-leap year so it has 365 days in it. The number of seconds per year is", nonLeapYear)