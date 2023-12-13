import random

print("This is a simple random number and grid generator. Bingo!")

# random.randint(1, 90) generates a random number between 1 and 90

# Generates a grid of 3 rows and 3 columns
grid = [
    [random.randint(1, 90), random.randint(1, 90), random.randint(1, 90)],
    [random.randint(1, 90), random.randint(1, 90), random.randint(1, 90)],
    [random.randint(1, 90), random.randint(1, 90), random.randint(1, 90)]
  ]

print(grid[0][0], " | ", grid[0][1], " | ", grid[0][2])
print("-" * 15)
print(grid[1][0], " | ", grid[1][1], " | ", grid[1][2])
print("-" * 15)
print(grid[2][0], " | ", grid[2][1], " | ", grid[2][2])