# Dynamically add to a [list]
my_agenda = []

def print_list():
  print() #this is just to add an extra space between items
  for item in my_agenda:
    print(item)
  print() #this is just to add an extra space between items
  
while True:
  item = input("What's next on the Agenda?: ")

# Appends to the list via .append(). The variable, "item," is the input variable. 
  my_agenda.append(item)
  print_list()
