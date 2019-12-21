from cursorColorama import *
import time

'''
Order of operation:
    per time step:
        update velocity by applying gravity
        update position of every moon by applying velocity
        progress time by 1 step

Gravity is changed according to following:
    for each x y z,
        if x1 is > x2
            Vx1 + 1
            Vx2 - 1
        elif x1 is < x2
            Vx1 - 1
            Vx2 + 1

Velocity is changed according to the following:
    for each x y z,
        x += Vx

Total energy is according to following:
    for each moon:
        for each Px:
            potential += abs(Px)
        for each Vx:
            kinetic += abs(Vx)
        energy += potential * kinetic


Input:
<x=15, y=-2, z=-6>
<x=-5, y=-4, z=-11>
<x=0, y=-6, z=0>
<x=5, y=9, z=6>
'''

class State:

    def __init__(self, moons):
        self.values = []
        for moon in moons:
            self.values.extend(moon.pos)
            self.values.extend(moon.vel)

    def equals(self, other):
        for ind, val in enumerate(self.values):
            if val != other.values[ind]:
                return False
        return True

class Moon:

    def __init__(self, name, x, y, z, colorInp = Fore.WHITE):
        self.color = colorInp
        self.name = name
        self.pos = [x, y, z]
        self.vel = [0, 0, 0]

    def __str__(self):
        out = self.color

        out += "Moon {}: pos <{},{},{}>, vel <{},{},{}>                       ".format(
        self.name,
        self.pos[0], self.pos[1], self.pos[2],
        self.vel[0], self.vel[1], self.vel[2])

        out += Fore.WHITE

        return out

    def updateGravity(self, moons):
        for moon in moons:
            for i in range(3):
                "0, 1, 2"
                if self.pos[i] < moon.pos[i]:
                    self.vel[i] += 1

                elif self.pos[i] > moon.pos[i]:
                    self.vel[i] -= 1
    def updatePosition(self):
        for i in range(3):
            self.pos[i] += self.vel[i]

    def updateGrav1d(self, moons, dimension):
        #dimension 0:x, 1:y, 2:z
        for moon in moons:
            if self.pos[dimension] < moon.pos[dimension]:
                self.vel[dimension] +=1
            elif self.pos[dimension] > moon.pos[dimension]:
                self.vel[dimension] -= 1

    def updatePos1d(self, moons, dimension):
        for moon in moons:
            self.pos[dimension] += self.vel[dimension]


moons = []
moons.append(Moon(1, 15, -2, -6, colorInp = Fore.RED))
moons.append(Moon(2, -5, -4, -11, colorInp = Fore.GREEN))
moons.append(Moon(3, 0, -6, 0, colorInp = Fore.LIGHTBLUE_EX))
moons.append(Moon(4, 5, 9, 6, colorInp = Fore.YELLOW))

#moons.append(Moon(1, -1, 0, 2, colorInp = Fore.RED))
#moons.append(Moon(2, 2, -10, -7, colorInp = Fore.GREEN))
#moons.append(Moon(3, 4, -8, 8, colorInp = Fore.LIGHTBLUE_EX))
#moons.append(Moon(4, 3, 5, -1, colorInp = Fore.YELLOW))


def printMoons():
    print("Moons at epoch {}: ".format(epoch))
    for moon in moons:
        print ("   ",moon)
    print("Total energy of system is", getEnergy(moons),"                      ")

def updateEach():
    for moon in moons:
        moon.updateGravity(moons)
    for moon in moons:
        moon.updatePosition()
    #time.sleep(0.05)

def update1d(dimension):
    for moon in moons:
        moon.updateGrav1d(moons, dimension)
    for moon in moons:
        moon.updatePosition()

def getEnergy(moons):
    energy = 0

    for moon in moons:
        pEng = 0
        kEng = 0
        for pos in moon.pos:
            pEng += abs(pos)
        for vel in moon.vel:
            kEng += abs(vel)
        energy += pEng * kEng

    return energy


'''
Functions stop here
'''

grid = []

temp = []
for i in range(100):
    temp.append(" ")

def updateGrid():
    grid.clear()
    for i in range(50):
        grid.append(temp.copy())
    for moon in moons:
        grid[moon.pos[1]][moon.pos[0]] = moon.color + "O"

def printGrid():
    for row in grid:
        for val in row:
            print(val+Fore.WHITE, end = "")
        print()

'''
Visual stops here
'''

states = {""}

epoch = 0
printMoons()
printGrid()


ind = 0
skipFrames = 1000

while True:
#    time.sleep(0.15)


    values = ""
    for moon in moons:
        values += str(moon.pos)
        values += str(moon.vel)


    if values in states:
        break
    else:
        states.add(values)

    if ind%skipFrames == 0:
        moveCursor(0,0)
        printMoons()
        #input()
    ind+=1
    epoch += 1
    update1d(1)

print("\nFinished\n")
printMoons()


#161428 on x
#167624 on y
#193052 on z

epochVal = 0

while True:
    moveCursor(50,5)
    print(epochVal)
    epochVal+=161428
    if epochVal % 161428 == 0:
        if epochVal % 167624 == 0:
            if epochVal % 193052 == 0:
                break
print(epochVal)

#its not 60135 lmao
# 326,489,627,728,984
