todo_list = []

# The subroutine for printing the Todo list. 
def print_list():
  print()

  # If the list is empty, indicate so. 
  if todo_list == []:
    print("The Todo List is empty.")

  # Otherwise . . .
  for item in todo_list:
    print(item)
    
  print()

print("----------------------------------")
print(" Welcome to the ToDo List Manager ")
print("----------------------------------")
print()

while True:

  # The menu selections. 
  list_menu = input("Do you want to view | add | edit your to do list? ").lower()

  if list_menu == "view":
    print_list()
      
  elif list_menu == "add":
    addition = input("What do you want to add? ")
    todo_list.append(addition)
    print_list()
    
  elif list_menu == "edit":
    print_list()
    edit = input("What do you want to remove? ")

    if edit in todo_list:
      todo_list.remove(edit)
      print_list()
      
    else:
      print(f"{edit} isn't in the list.")
      print_list()

  
  