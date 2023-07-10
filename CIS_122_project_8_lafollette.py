import turtle as mazeTurtle
import time

heightN = int(input("Enter height: "))
widthM = int(input("Enter width: "))

mazeVar = []

for i in range(heightN):
    mazeVar.append(input("Enter rows: "))
    
coordX = -1
coordY = -1

for i in range(heightN):
    for j in range(widthM):
        if mazeVar[i][j] == "R":
            visited = {(-1,-1)}
            coordX = i
            coordY = j
            
def escapeMaze(y,x):
    
    if (y,x) in visited:
        return False
    
    visited.add((y,x))
    
    if x < 0 or y < 0 or x >= widthM or y >= heightN:
        return ("DONE",)
    
    for i in {(-1, 0, "UP"),(1, 0, "DOWN"),(0, 1, "RIGHT"),(0, -1, "LEFT")}:
        
        if (y+i[0] >= 0 and y + i[0] < heightN and x+i[1] >= 0 and x+i[1] < widthM and mazeVar[y+i[0]][x+i[1]] != "S"):
            possibleAnswer = escapeMaze(y+i[0], x+i[1])
            
            if possibleAnswer != False:
                return (i[2],) + possibleAnswer
            
    return False

t = escapeMaze(coordY, coordX)
t = t[0:len(t) - 1]

for i in range(len(t)):
    
    if t[i] == "UP":
        mazeTurtle.setheading(90)
        mazeTurtle.fd(15)
        time.sleep(1)
        
    elif t[i] == "DOWN":
        mazeTurtle.setheading(270)
        mazeTurtle.fd(15)
        time.sleep(1)
        
    elif t[i] == "LEFT":
        mazeTurtle.setheading(180)
        mazeTurtle.fd(15)
        time.sleep(1)
        
    elif t[i] == "RIGHT":
        mazeTurtle.setheading(0)
        mazeTurtle.fd(15)
        time.sleep(1)
