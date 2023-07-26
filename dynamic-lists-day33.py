# Dynamically add to a [list]
my_agenda = []

def print_list():
  
  print() #this is just to add an extra space between items
  
  for item in my_agenda:
    print(item)
    
  print() #this is just to add an extra space between items
  
while True:
  
  menu = input("add or remove?: ")
  
  if menu == "add":
    item = input("What's next on the Agenda?: ")
    my_agenda.append(item)
    
  elif menu == "remove":
    item = input("What do you want to remove?: ")
    my_agenda.remove(item)
    
  print_list()
