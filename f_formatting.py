print("30 Days down - what do you think so far?")
print()
for i in range(1, 31):
  # Input question - use format.
  your_response = input(f"Day {i} was: ")
  
  print()
  
  response = f"You thought Day {i} was"
  
  # Formatting to center the next
  print(f"{response:^40}")

  # Formatting to center the next
  print(f"{your_response:^40}")
  print()

