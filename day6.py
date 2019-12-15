orbits = []
with open("day6.txt") as file:
    data = file.read()
    orbits = data.splitlines()
for i in range(len(orbits)):
    orbits[i] = orbits[i].split(")")

class Planet:

    def __init__(self, name, parent = 0):
        self.name = name
        self.parent = parent
        self.children = []

    def __str__(self):
        try:
            return ("Planet {}, with {} children, first child:\n{}".format(self.name, len(self.children), self.children[0]))
        except:
            return ("Planet {}, with no children.".format(self.name))

    def steps(self):
        temp = self
        steps = 0
        while(temp.name != "COM"):
            steps+=1
            temp = temp.parent
        return steps


def planetInList(list,name):
    for planet in list:
        if planet.name == name:
            return True
    return False

def getPlanetInList(list, name):
    for planet in list:
        if planet.name == name:
            return planet
    return 0


planets = [Planet("COM")]


for i in orbits:
    name = i[0]
    if not planetInList(planets, name):
        planets.append(Planet(name))
    name = i[1]
    if not planetInList(planets, name):
        planets.append(Planet(name))
#By now, all planets are added, but no parents or children

for orbit in orbits:
    parent = getPlanetInList(planets, orbit[0])
    child = getPlanetInList(planets, orbit[1])
    parent.children.append(child)
    child.parent = parent

#print(getPlanetInList(planets,"COM").children[0])
sum = 0
for a in planets:
    sum += a.steps()
print(sum)
