print("---------------------")
print(" Replit Login System")
print("---------------------")
print()

def userLogin():
  while True:
    userName = input("What is your username? > ").lower()
    passWord = input("What is your password? > ")

    if userName != "david":
      print("Wrong username. Try again!")
      continue

    elif passWord != "baldies4life":
      print("Wrong password. Try again!")
      continue
  
    if userName == "david" and passWord == "baldies4life":
      print("Welcome to Replit!")
      break
      
userLogin()