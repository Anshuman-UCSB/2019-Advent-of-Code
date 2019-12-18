import math

import numpy as np

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    phi = math.degrees(phi)
    phi += 90
    while phi<0:
        phi+=360
    while phi>360:
        phi-=360
    return (rho, phi, x, y)

space = []
with open("day10.txt") as file:
    data = file.read()

class Space:

    def __init__(self, data):
        self.grid = data.splitlines()
        for i in range(len(self.grid)):
            self.grid[i] = list(self.grid[i])

        self.xMax = len(self.grid[0])
        self.yMax = len(self.grid)
        self.modGrid = []
        for row in self.grid:
            self.modGrid.append(row.copy())
        self.asteroids = []

        for x in range(self.xMax):
            for y in range(self.yMax):
                if self.grid[y][x] != ".":
                    self.asteroids.append((x,y))
                    #print("{}, {}".format(x, y))

    def printGrid(self):
        print()
        for row in self.grid:
            for char in row:
                print (char, end = "")
            print()
        print()

    def printMod(self):
        print()
        for row in self.modGrid:
            for char in row:
                print (char, end = "")
            print()
        print()

    def distance(self, a1, a2):
        return (a2[0]-a1[0],a2[1]-a1[1])

    def slope(self, a1, a2):
        x = a2[0] - a1[0]
        y = a1[1] - a2[1]

        if(x<0):
            sign = -1
        elif(x>0):
            sign = 1
        elif(y<0):
            sign = -1
        else:
            sign = 1

        try:
            slope = y/x
        except:
            slope = "INF"

        dist = abs(x) + abs(y)

        ret = [x, y, slope, sign, dist]

        return ret

space = Space(data)
space.printGrid()

center = (22,28) #actual
debug = (8,4)

polar = []

ang = 0


def compare(c1, c2):
    if c1[1] < c2[1]:
        return True
    elif c1[1] == c2[1]:
        if c1[0] > c2[0]:
            return False
        else:
            return True
    else:
        return False

def sortList(list):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(list)-1):
            if not compare(list[i],list[i+1]):
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
                sorted = False

for asteroid in space.asteroids:
    xy = space.distance(debug, asteroid)
    polar.append(cart2pol(xy[0],xy[1]))

#for i in range(len(polar)):
    #print(math.degrees(polar[i][1]))

#polar.remove((0,90,0,0))

angles = []
Los = []

print("\nPresort:")
for a in polar:
    print(" > "+str(a))

sortList(polar)
print("\nPostsort:")
for a in polar:
    print(" > "+str(a))

print()

for elem in polar:
    if not elem[1] in angles:
        angles.append(elem[1])


for angle in angles:
    smallest = (9999,angle)
    for elem in polar:
        if elem[1] == angle and elem[0]<smallest[0] and elem[0] > 0:
            smallest = elem
    Los.append(smallest)

rays = []
for angle in angles:
    rays.append([])

for elem in polar:
    rays[angles.index(elem[1])].append(elem)


print("\nRays:")
for a in rays:
    print(" > "+str(a))
print()
print("\nAngles:")
print(angles)
print()

print("LOS:")
for a in Los:
    print(" > "+str(a))
print()

visual = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

empty = False
ind = 0
i = 0

def nestedEmpty(list):
    for row in list:
        if len(row)>0:
            return False
    return True

while not nestedEmpty(rays):
    try:
        val = rays[ind%len(rays)].pop(0)
        space.modGrid[val[3]+2][2+val[2]]=visual[i]
        i+= 1
        print("{}: {}".format(visual[i],val))
    except:
        pass
    ind+=1

print()
print("Mod grid:")
space.printMod()
space.printGrid()
