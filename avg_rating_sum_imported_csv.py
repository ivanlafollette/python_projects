# Calculate the average app rating for all of the 7,197 apps stored in our dataset.

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

# The intial empty list. 
rating_sum = []

for row in apps_data[1:]:
    rating = float(row[7])
    rating_sum.append(rating)
    avg_rating = sum(rating_sum) /  len(rating_sum)
    print(avg_rating)