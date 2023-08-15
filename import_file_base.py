# Import file base

opened_file = open('AppleStore.csv')

from csv import reader

read_file = reader(opened_file)

apps_data = list(read_file)

