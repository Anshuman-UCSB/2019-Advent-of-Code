import numpy as np
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
    print("  Astr {}: {}".format(astr, len(angles)))
    modGrid[astr[1]][astr[0]] = len(angles)

for row in modGrid:
    for val in row:
        print(val, end = "")
    print()
