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

class space:

    def __init__(self):
        with open("day10.txt") as file:
            data = file.read()
        data = data.splitlines()
        self.grid = []
        for row in data:
            self.grid.append(list(row))

        self.modGrid = copy.deepcopy(self.grid)

        self.asteroids = []
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.grid[y][x] == "#":
                    self.asteroids.append(asteroid(x,y))


    def __str__(self):
        print("    Grid: ")
        for row in self.grid:
            for val in row:
                print(val,end = "")
            print()
        print()
        print("    Asteroids: ")
        for asteroid in self.asteroids:
            print(asteroid)
        return("")

    def getVisible(self, asteroid):
        for astr in self.asteroids:
            astr.setRel(asteroid)
        sortAstr(self.asteroids)
        for astr in self.asteroids:
            print(astr.relPolar)

        angles = []
        for astr in self.asteroids:
            if not astr.relPolar[1] in angles:
                angles.append(astr.relPolar[1])
        print(angles)

class asteroid:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xy = [x,y]

        self.polar = cart2pol(x,y)
        self.r = self.polar[0]
        self.phi = self.polar[1]

    def setRel(self, asteroid):
        self.relX = self.x-asteroid.x
        self.relY = self.y-asteroid.y

        self.relPolar = cart2pol(self.relX, self.relY)

    def __str__(self):
        return " > Cartesian: ({}, {}) <> Polar: ({}, {})".format(self.x,self.y,self.r,self.phi)

def compareAstr(a1, a2):
    print("comparing {} and {}".format(a1.relPolar,a2.relPolar))
    if a1.relPolar[1] >= 270 and a2.relPolar[1] <270:
        return True
    if a1.relPolar[1] <270 and a1.relPolar[1] >= 270:
        return False
    return a1.relPolar[1]<a2.relPolar[1]

def sortAstr(list):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(len(list)-1):
            if compareAstr(list[i], list[i+1]):
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
                sorted = False


spc = space()
print(spc)
spc.getVisible(asteroid(1,1))
