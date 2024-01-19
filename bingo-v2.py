import random

print("Let's play some Bingo!")
print()

bingo = 0

while bingo < 5:
# random.randint(1, 90) generates a random number between 1 and 90

  def ballcall():
    number = random.randint(1, 90)
    return number
  
  ballcall()
  # Generates a grid of 5 rows and 5 columns from lists.
  print("The first number is...", number)
  
  grid = [
      [random.randint(1, 90), random.randint(1, 90), random.randint(1, 90), random.randint(1, 90), random.randint(1, 90)],
      [random.randint(1, 90), random.randint(1, 90), random.randint(1, 90), random.randint(1, 90), random.randint(1, 90)],
      [random.randint(1, 90), random.randint(1, 90), random.randint(1, 90), random.randint(1, 90), random.randint(1, 90)],
      [random.randint(1, 90), random.randint(1, 90), random.randint(1, 90), random.randint(1, 90), random.randint(1, 90)],
      [random.randint(1, 90), random.randint(1, 90), random.randint(1, 90), random.randint(1, 90), random.randint(1, 90)]
    ]
  
  
  print(" B     I      N      G      O")
  print("-" * 30)
  print(grid[0][0], " | ", grid[0][1], " | ", grid[0][2], " | ", grid[0][3], " | ", grid[0][4])
  print("-" * 30)
  print(grid[1][0], " | ", grid[1][1], " | ", grid[1][2], " | ", grid[1][3], " | ", grid[1][4])
  print("-" * 30)
  print(grid[2][0], " | ", grid[2][1], " | ", grid[2][2], " | ", grid[2][3], " | ", grid[2][4])
  print("-" * 30)
  print(grid[3][0], " | ", grid[3][1], " | ", grid[3][2], " | ", grid[3][3], " | ", grid[3][4])
  print("-" * 30)
  print(grid[4][0], " | ", grid[4][1], " | ", grid[4][2], " | ", grid[4][3], " | ", grid[4][4])

        