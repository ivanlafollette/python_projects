# Lists
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.99, 'USD', 698516, 4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012, 4.5]

# A list of lists. 
app_data_set = [row_1, row_2, row_3, row_4, row_5]

# This is an empty variable that will be used to summarize the rating points. 
a_sum = 0

# The row interation variable will loop over the app_data_set list of list. 
for row in app_data_set:
    # The interization of the ratings (at the -1 position) will be added to a_sum
    a_sum += row[-1]
    # We'll see each iteration added. 
    print(a_sum)
 
# The final summary will be printed. 
print(a_sum)