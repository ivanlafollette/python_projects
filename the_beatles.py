# step 1
# First, we create an empty list. 

beatles = []
print("Step 1:", beatles)
print("Looks pretty empty. Let's add some members to it.")

# step 2

# Append the names of the Beatles to the Beatlest list using the append() method. 
beatles_members1 = input("Add John Lennon: ")
beatles.append(beatles_members1) 

beatles_members2 = input("Add Paul McCartney: ")
beatles.append(beatles_members2) 

beatles_members3 = input("Add George Harrison: ")
beatles.append(beatles_members3) 

print("Step 2:", beatles)

# step 3

print("Okay, we aren't done here. Add Stu SutCliffe and Pete Best to the band.")

for _ in range(2):
    old_beatles1 = input("Add one, and then the other: ")
    beatles.append(old_beatles1)
    
print("Step 3:", beatles)

# step 4
print("Now, those guys left the band, so let's get rid of them.")
remove_stu = input("Remove Stu Sutcliffe from the band. ")
beatles.remove(remove_stu)

remove_stu = input("Remove Pete Best from the band. ")
beatles.remove(remove_stu)

print("Step 4:", beatles)

# step 5

print("Now, we have to add the great Ringo to the band. ")
add_ringo = input("Go ahead and add Ringo Starr: ")

# The first argument is the element location in the list. 
beatles.insert(3, add_ringo)

print("Step 5:", beatles)

# testing list legth
print("Now, we have the complete Beatles. The one, the only!")
print("The Fab", len(beatles))
print("I hope you're happy, Greg!")
