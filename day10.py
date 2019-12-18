import math

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
        self.modGrid = self.grid.copy()
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
        return (a1[0]-a2[0],a2[1]-a1[1])

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
#print(space.asteroids)

for i in range(len(space.asteroids)):
    slopes = []
    for asteroid in space.asteroids:
        slopes.append(space.slope(space.asteroids[i], asteroid))

    for slope in slopes:
        if slope[4] == 0:
            slopes.remove(slope)

    LOSslopes = []
    #print()
    print("    Asteroid {}".format(space.asteroids[i]))

    for j in range(len(slopes)):
        linear = []
        slp = slopes[j][2]
        side = slopes[j][3]
        for slope in slopes:
            if slope[2] == slp and slope[3] == side:
                linear.append(slope)

        #print(linear)
        minSlp = linear[0]
        for slp in linear:
            if slp[4]<minSlp[4]:
                minSlp = slp
        LOSslopes.append(minSlp)
        #print("     Linear: "+str(linear))
    clean = []
    [clean.append(x) for x in LOSslopes if x not in clean]

    LOSslopes = clean
    visible = len(LOSslopes)

    #print(visible)
    space.modGrid[space.asteroids[i][1]][space.asteroids[i][0]]=visible
    #for thing in LOSslopes:
        #print("LOS "+str(thing))

    #print()
    #for thing in slopes:
        #print (thing)


space.printMod()

values = []

for row in space.modGrid:
    for val in row:
        try:
            values.append(int(val))
        except:
            pass

print(values)
print("Max: "+str(max(values)))













exit() #stinky code
ind = 0
for ind in range(len(space.asteroids)):
    asteroid = space.asteroids[ind]
    #print(asteroid)
    slopes = []
    LOSslopes = []
    for i in range(0,len(space.asteroids)):
        slopes.append(space.slope(space.distance(asteroid, space.asteroids[i])))

    slopes.pop(ind)

    for i in range(len(slopes)):
        slp = slopes[i]
        for slope in slopes:
            if slope[0] == slp[0] and slope[2] < slp[2]:
                slp = slope
        LOSslopes.append(slp)
    clean = []
    [clean.append(x) for x in LOSslopes if x not in clean]

    LOSslopes = clean
    print("Asteroid {}, {}".format(asteroid,len(LOSslopes)))
    space.modGrid[asteroid[1]][asteroid[0]] = len(LOSslopes)

values = []
for row in space.modGrid:
    for val in row:
        try:
            values.append(int(val))
        except:
            pass

space.printMod()
print(max(values))
