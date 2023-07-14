print("--------------")
print("   Math Game  ")
print("--------------")
print()
print("We're going to create muliplication tables Let's see how many you get right.")
print()
multiples = int(input("Name your mulitples: "))
print()

right = 0
counter = 1
for counter in range(1, 11):
  
  answer = multiples * counter 
  print("What is", counter, "x", multiples, "?")
  question = int(input(" > "))

  if question != answer:
    print("Nope. The answer is", answer)
  
  elif question == answer:
    right += 1
    print("You got it right! Awesome")

  print()
  if counter == 10:
    print("-----------")
    print("All done!")
    print("You scored", right, "out of", 10)
