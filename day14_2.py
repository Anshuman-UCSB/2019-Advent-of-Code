data = """9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL
"""

with open("day14.txt") as file:
    data = file.read()
    pass

info = data.splitlines()
print("Recipies:")
for line in info:
    print(" ",line)

recipies = []
quantity = {"ORE":0}

for line in info:
    recip = line.split(" => ")
    recip[0] = recip[0].split(", ")
    for ind, val in enumerate(recip[0]):
        recip[0][ind] = recip[0][ind].split(" ")
        recip[0][ind][0] = int(recip[0][ind][0])
    recip[1] = recip[1].split(" ")
    recip[1][0] = int(recip[1][0])

    recipies.append(recip)

def getRecipie(prod):
    if prod == "ORE":
        return "ORE"
    for recipie in recipies:
        if recipie[1][1] == prod:
            return recipie
    return -1

def makeMultiple(prod, count):
    recipie = getRecipie(prod)
    #print(recipie)
    #print("Here is the recipie for "+ prod)
    if recipie != "ORE" and recipie != -1:
        #valid recipie
        quantity[recipie[1][1]] += count*recipie[1][0]
    for reactant in recipie[0]:
        quantity[reactant[1]] -= count*reactant[0]

def makeOne(prod):
    recipie = getRecipie(prod)
    #print(recipie)
    #print("Here is the recipie for "+ prod)
    if recipie != "ORE" and recipie != -1:
        #valid recipie
        quantity[recipie[1][1]] += recipie[1][0]
    for reactant in recipie[0]:
        quantity[reactant[1]] -= reactant[0]

def hasNegative():
    for key, value in quantity.items():
        if key != "ORE" and value < 0:
            #print("neg",key)
            return True
    return False

def makeNegatives():
    for key, value in quantity.items():
        if key != "ORE" and value < 0:
            #print("Making key {}, because quantity is {}".format(key, value))
            #print("Using recipie", getRecipie(key))
            recip = getRecipie(key)
            needed = 0
            while needed < abs(value):
                needed += recip[1][0]
                #print(needed)
            needed/= recip[1][0]
            needed = int(needed)
            #print("Making",needed)
            #lets say it needs 8
            #recipie makes 5
            #should make 10
            makeMultiple(key, needed)


"""
recipie[1] = products
recipie[0] = Reactants
recipie[0][0] = first reactant
recipie[0][0][0] = # first reactant
recipie[0][0][1] = reactant name
"""

for recipie in recipies:
    #print (recipie)
    quantity[recipie[1][1]] = 0
print()
print("Quantities:",quantity)

print()

countsOF = []
make = 1000000

ore_count = 1_000_000_000_000

#makeMultiple("FUEL",2168)
#while(hasNegative()):
    #makeNegatives()

ind = 0
skipFrame = 1

while quantity["ORE"]>(0-ore_count):
    makeMultiple("FUEL",make)
    make = int(make/1.15)
    if make<1:
        make = 1
    while(hasNegative()):

        makeNegatives()
    countsOF.append((ore_count+quantity["ORE"],quantity["FUEL"]))
    if ind%skipFrame == 0:
        print(countsOF[len(countsOF)-1])
    ind+= 1

print()
print("Quantities:",quantity)
print(countsOF)

"2168 is too low"
"2169 not it either?"
