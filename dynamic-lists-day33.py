# Dynamically add to a [list]
my_agenda = []

def printList():
  print() #this is just to add an extra space between items
  for item in my_agenda:
    print(item)
  print() #this is just to add an extra space between items
  
while True:
  item = input("What's next on the Agenda?: ")

# Appends to the list via .append()
  my_agenda.append(item)
  printList()
