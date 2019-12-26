from cursorColorama import *

with open("day15maze.txt") as file:
    maze = eval(file.read())

colors = [Fore.WHITE, Fore.BLACK, Fore.LIGHTBLUE_EX]

for y, row in enumerate(maze):
    for x, val in enumerate(row):
        if val == 2:
            maze[y][x] = 0
        elif val == 3:
            maze[y][x] = 2

def printGrid():
    moveCursor(0,0)
    for row in maze:
        for val in row:
            if val == 0:
                print(colors[1]+"█",end = Fore.WHITE)
            elif val == 1:
                print(colors[0]+"█",end = Fore.WHITE)
            elif val == 2:
                print(colors[2]+"█",end = Fore.WHITE)
        print()

iteration = [0]

def setAdjacent(coord):
    possible = []
    possible.append([coord[0]-1, coord[1]])
    possible.append([coord[0]+1, coord[1]])
    possible.append([coord[0], coord[1]+1])
    possible.append([coord[0], coord[1]-1])

    for pos in possible:
        if maze[pos[1]][pos[0]] == 0:
            maze[pos[1]][pos[0]] = 3

def iterate():
    iteration[0]+=1
    for y, row in enumerate(maze):
        for x, val in enumerate(row):
            if val == 2:
                setAdjacent([x,y])
    for y, row in enumerate(maze):
        for x, val in enumerate(row):
            if val == 3:
                maze[y][x] = 2

printGrid()
while True:
    input()
    iterate()
    printGrid()
    print("Iteration",iteration[0])

#392 iterations
