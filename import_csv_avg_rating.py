opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

rating_sum = 0
# Loop through the apps_data lists of lists excluding the first row. 
for row in apps_data[1:]:
    # Extra the rating data (it has an index of [7]), and convert to a float. 
    rating = float(row[7])
    # Add values. 
    rating_sum = rating_sum + rating
    # Average the ratings
    avg_rating = rating_sum / 7197

print(avg_rating)