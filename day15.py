from processor import processor
from cursorColorama import *


with open("day15.txt") as file:
    code = file.read()
code = code.split(",")
for i, val in enumerate(code):
    code[i] = int(val)
prc = processor(code)
prc.pad(1000)

print(prc)

graphics = ["D",".","#","O"]
"            0   1   2   3 "
"droid, empty, wall, oxygen"

grid = []
size = [30,50]
loc = [int(size[1]/2),int(size[0]/2)]
temp = [" "]*size[1]
for i in range(size[0]):
    grid.append(temp.copy())

def draw(loc, char):
    x = loc[0]
    y = loc[1]
    if char == "D":
        grid[y][x]+=char
    else:
        grid[y][x] = char

pad = "             "
def printGrid():
    moveCursor(0,0)
    print(pad, end = "")
    print("#"*(len(grid[0])+2))
    for row in grid:
        print(pad, end = "")
        print("#", end ="")
        for val in row:
            print(val, end = "")
        print("#",pad)
    print(pad, end = "")
    print("#"*(len(grid[0])+2))


def move(dir):
    prc.inputs.append(dir)
    while len(prc.outputs) < 1:
        prc.process()
    response = prc.outputs.pop(0)
    grid[loc[1]][loc[0]] = grid[loc[1]][loc[0]][0]
    if response == 1:
        if dir == 1:
            loc[1] -= 1
        if dir == 2:
            loc[0] += 1
        if dir == 3:
            loc[1] += 1
        if dir == 4:
            loc[0] -= 1
        draw(loc,"D")
    if response == 0:
        if 

    return response


input("resize and press enter")
draw(loc,".")
draw(loc,"D")
status = "NONE"
while not prc.finished:
    while status != "Waiting on input":
        status = prc.process()
    printGrid()
    move(1)
