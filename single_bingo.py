import random

print("Let's play some bingo!")
print()
# random.randint(1, 90) generates a random number between 1 and 90

# Generates a grid of 3 rows and 3 columns
# This is really inefficient. I need to use loops and functions to make this better. 
picks1 = [
    [random.randint(1, 25), random.randint(1, 25), random.randint(1, 25), random.randint(1, 25), random.randint(1, 25)]
    ]
picks2 = [
    [random.randint(1, 25), random.randint(1, 25), random.randint(1, 25), random.randint(1, 25), random.randint(1, 25)]
    ]
picks3 = [
    [random.randint(1, 25), random.randint(1, 25), random.randint(1, 25), random.randint(1, 25), random.randint(1, 25)]
    ]
picks4 = [
    [random.randint(1, 25), random.randint(1, 25), random.randint(1, 25), random.randint(1, 25), random.randint(1, 25)]
    ]
picks5 = [
    [random.randint(1, 25), random.randint(1, 25), random.randint(1, 25), random.randint(1, 25), random.randint(1, 25)]
    ]

print("-" * 28)
print(picks1[0][0], " | ", picks1[0][1], " | ", picks1[0][2], " | ", picks1[0][3], " | ", picks1[0][4])
print("-" * 28)
print(picks2[0][0], " | ", picks2[0][1], " | ", picks2[0][2], " | ", picks2[0][3], " | ", picks2[0][4])
print("-" * 28)
print(picks3[0][0], " | ", picks3[0][1], " | ", picks3[0][2], " | ", picks3[0][3], " | ", picks3[0][4])
print("-" * 28)
print(picks4[0][0], " | ", picks4[0][1], " | ", picks4[0][2], " | ", picks4[0][3], " | ", picks4[0][4])
print("-" * 28)
print(picks5[0][0], " | ", picks5[0][1], " | ", picks5[0][2], " | ", picks5[0][3], " | ", picks5[0][4])
print("-" * 28)