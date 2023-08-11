# Calculating the height of persons from lists using a for loop, len(), an if statement, division, and round().
# Data
people = [["Alex", 178], ["Noah", 189], ["Peter", 175], ["John", 185], ["Michelle", 165]]

# Iterating over external list
for i in range(len(people)):
    if type(people[i]) is list:
        # Calculate and round height in inches
        ht_in = round(people[i][1]/2.54, 2)
        print(people[i][0], 'has height of', ht_in, 'inches')