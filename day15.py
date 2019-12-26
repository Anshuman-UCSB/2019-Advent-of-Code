from processor import processor
from cursorColorama import *
import random

with open("day15.txt") as file:
    code = file.read()
code = code.split(",")
for i, val in enumerate(code):
    code[i] = int(val)
prc = processor(code)
prc.pad(1000)

print(prc)

graphics = ["D","░","█","O"]
"            0   1   2   3 "
"droid, empty, wall, oxygen"

grid = []
size = [40,42]
loc = [int(size[1]/2),int(size[0]/2)]
starting_loc = loc.copy()
temp = [" "]*size[1]
for i in range(size[0]):
    grid.append(temp.copy())

def draw(loc, char):
    #print("drawing",char,"at",loc)
    x = loc[0]
    y = loc[1]
    if char == "D":
        grid[y][x]+=char
        #print("Setting d:",grid[y][x])
    if char == "":
        #print(grid[y][x],"<")
        grid[y][x] = grid[y][x][0:1]
    else:
        grid[y][x] = char

pad = "             "
def printGrid():
    moveCursor(0,0)
    print(pad, end = "")
    print("█"*(len(grid[0])+2))
    for row in grid:
        print(pad, end = "")
        print("█", end ="")
        for val in row:
            char = val[-1]
            if char == "D":
                print(Fore.RED,end="")
            if char == "O":
                print(Fore.LIGHTBLUE_EX,end="")
            if char == "▓":
                print(Fore.GREEN,end="")
            print(char, end = "")
            print(Fore.WHITE, end="")
        print("█",pad)
    print(pad, end = "")
    print("█"*(len(grid[0])+2))

steps = [0]

def move(dir):
    steps[0]+=1
    prc.inputs.append(dir)
    while len(prc.outputs) < 1:
        prc.process()
    response = prc.outputs.pop(0)
    moveCursor(100,20)
    print("Moving {}, got response {}.".format(dir,response))

    if response == 1:
        draw(loc,"")
        if dir == 1:
            loc[1] -= 1
        if dir == 2:
            loc[1] += 1
        if dir == 3:
            loc[0] -= 1
        if dir == 4:
            loc[0] += 1
        draw(loc,"░D")
    if response == 0:
        if dir == 1:
            draw([loc[0],loc[1]-1], "█")
        if dir == 2:
            draw([loc[0],loc[1]+1], "█")
        if dir == 3:
            draw([loc[0]-1,loc[1]], "█")
        if dir == 4:
            draw([loc[0]+1,loc[1]], "█")
    if response == 2:
        draw(loc,"")
        if dir == 1:
            loc[1] -= 1
        if dir == 2:
            loc[1] += 1
        if dir == 3:
            loc[0] -= 1
        if dir == 4:
            loc[0] += 1
        draw(loc,"OD")


    return response


input("resize and press enter")

draw(loc,"▓D")
status = "NONE"
facing = 0

frame= 0
skipframe = 50

def fillGrid():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == " ":
                grid[i][j] = "█"

while not prc.finished:
    while status != "Waiting on input":
        status = prc.process()
    if frame%skipframe==0:
        printGrid()
    frame+=1

    choices = [1,4,2,3]
    #input("facing "+str(choices[facing]))

    if move(choices[(facing+1)%4]) == 1:
        #print("Wall on right")
        if move(choices[facing]) == 1:
            #print("Wall in front")
            facing+=3
    else:
        facing+=1
    facing %= 4
    if loc == starting_loc and steps[0]>10:
        fillGrid()
        printGrid()

        moveCursor(100,42)
        print("finished maze?")
        break
    #input("Now facing"+str(choices[facing]))

maze = []
temp = [-1] * len(grid[0])
for i in range(len(grid)):
    maze.append(temp.copy())
for x in range(len(grid[0])):
    for y in range(len(grid)):
        gridVal = grid[y][x]
        translate = ["░","█","▓","O"]
        translateChar = -1
        for ind,char in enumerate(translate):
            if char in gridVal:
                translateChar = ind
        maze[y][x] = translateChar
    #input(chc)
maze[starting_loc[1]][starting_loc[0]] = 2
maze.insert(0,[1]*len(grid[0]))
for row in maze:
    for val in row:
        print(val,end="")
    print()
with open("day15maze.txt", "w") as file:
    file.write(str(maze))
