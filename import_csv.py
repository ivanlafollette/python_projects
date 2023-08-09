# The process is open() --> reader() --> list()

# From to import
from csv import reader

# Use open() to open the desired file, AppleStore.csv.
opened_file = open('AppleStore.csv')
# Place the reader() function in the reader_file variable.
read_file = reader(opened_file)

# The original code. This causes an error since the heaer is a string.
apps_data = list(read_file)

# This is the header row. 
header = apps_data[0]
# A list slice that excludes the first row.
apps_data = apps_data[1:]

print(apps_data[1])
print(apps_data[1][7])
print(type(apps_data[1][7]))

# Create an empty variable.
rating_sum = 0
# Create a for loop to iterate over apps_data.
for row in apps_data:
    
    rating = row[7]
    
    rating_sum = rating_sum + float(rating)
    print(rating_sum)