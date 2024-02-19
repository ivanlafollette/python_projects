# step 1
beatles = []
print("Step 1:", beatles)
print()
# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print()

print("Step 2:", beatles)

# step 3

for i in beatles:
    add_beatle = input("Add Stu Sutcliffe to the band: ")
    beatles.append(add_beatle)
    add_beatle2 = input("Good. Now add Pete Best: ")
    beatles.append(add_beatle2)
    break

print("Step 3 - this is how the band looks now: ", beatles)
print()
# step 4
print("Now, let's remove these members.")

del beatles[-1]
del beatles[-1]
print("Step 4:", beatles)

# step 5
print()
print("Now, last but not least, we add Ringo to the band.")

r_star = "Ringo Star"

beatles.insert(0, r_star)
print()
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))
