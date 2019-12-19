import numpy as np
import copy
import math

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    phi = math.degrees(phi)
    while phi<0:
        phi+=360
    return[rho, phi%360]
grid = []
modGrid = []
with open("day10.txt") as file:
    data = file.read()
data = data.splitlines()

for line in data:
    grid.append(list(line))
    modGrid.append(list(line))

for row in grid:
    for val in row:
        print(val, end = "")
    print()

asteroids = []

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "#":
            asteroids.append([x,y])

'''
By here, grid is initialized and asteroids has list of coords
'''

for astr in asteroids:
    others = asteroids.copy()
    others.remove(astr)
    #print(others)
    polar = []
    for elem in others:
        polar.append(cart2pol(elem[0]-astr[0],elem[1]-astr[1]))

    angles = []
    for elem in polar:
        if not elem[1] in angles:
            angles.append(elem[1])
    #print("  Astr {}: {}".format(astr, len(angles)))
    modGrid[astr[1]][astr[0]] = len(angles)

for row in modGrid:
    for val in row:
        print(val, end = "")
    print()

max = -1
maxCoord = []

for y in range(len(grid)):
    for x in range(len(grid[0])):
        try:
            if modGrid[y][x] > max:
                maxCoord = [x,y]
                max = modGrid[y][x]
        except:
            pass
print(maxCoord)

'''
Part 2 begins below
'''


others = asteroids.copy()
others.remove(maxCoord)
#print(others)
polar = []
for elem in others:
    polar.append(cart2pol(elem[0]-maxCoord[0],elem[1]-maxCoord[1]))

angles = []
for elem in polar:
    if not elem[1] in angles:
        angles.append(elem[1])


sorted = False
while not sorted:
    sorted = True
    for i in range(len(angles)-1):
        a1 = angles[i]
        a2 = angles[i+1]
        a1+=90
        a2+=90
        a1 %= 360
        a2 %= 360
        if a1 > a2:
            temp = angles[i]
            angles[i] = angles[i+1]
            angles[i+1] = temp
            sorted = False



print("Angles: ")
for angle in angles:
    print(" > "+str(round(angle, 3)))

rays = []
for angle in angles:
    rays.append([])
for i in range(len(polar)):
    rays[angles.index(polar[i][1])].append(others[i])

print("Rays:")
for ray in rays:
    print("  {}".format(ray))

def distance(a1, a2):
    return abs(a2[1]-a1[1]) + abs(a2[0]-a1[0])

def sortDist(list):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(list)-1):
            a1 = distance(maxCoord, list[i])
            a2 = distance(maxCoord, list[i+1])
            if a1 > a2:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
                sorted = False

for ray in rays:
    sortDist(ray)
    print(ray)

def emptyRays():
    for ray in rays:
        if len(ray)>0:
            return False
    return True

order = []

ind = 0
while not emptyRays():
    val = -1
    while val == -1:
        try:
            order.append(rays[ind%len(rays)].pop(0))
            val = 1
        except:
            pass
        ind+=1

print(order)
visible = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
modGrid = copy.deepcopy(grid)
index = 0
for i in range(10):
    elem = order[i]
    modGrid[elem[1]][elem[0]] = visible[index]
    index+=1
print()
print()
print()
modGrid[28][22] = 0
for row in modGrid:
    for val in row:
        print(val, end = "")
    print()

print()
print(order[199])
