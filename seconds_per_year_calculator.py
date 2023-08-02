"""
This module will calculate the number of seconds per minute, day, month, and year.
"""
# I renamed the variables to include an underscore, so that's why the code may have issues later on. Added - 8/1/2023

print("Tell me a year and I will extrapolate the number of seconds per year.")
print()
year_VAR = int(input("What year do you want to know about? "))
print()

# The calculation for the seconds per minute.
seconds_var = 60
minutes_var = 60
secs_minute = 60 * 60
print("The number of seconds per minute:", secs_minute)
print()

# The calculation for the seconds per hour.
secs_hour = secs_minute * 60
print("The number of seconds per hour:", secs_hour)
print()

# And the seconds per day.
day_hours = 24
secs_day = secs_hour * 24
print("The number of seconds per day:", secs_day )

# Now, using the seconds per day for the month.
secs_month = secs_day * 31
print()
print("The seconds per month:", secs_month)

print()

# Calculate if a year is a leap year. Is it divisible by 4 or 100 or 400? if so, run the following code.
if (year_VAR % 4 == 0 and year_VAR % 100 != 0) or year_VAR % 400 == 0:
  leap_year = 366 * secs_month
  print("This is a leap year so it has 366 days in it. The number of seconds per year is", leap_year)
  
# If not, then run the following code. 
else:
  non_leap_year = 365 * secs_month
  print("This is a non-leap year so it has 365 days in it. The number of seconds per year is", non_leap_year)
