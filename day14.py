from cursorColorama import *
import random

with open("day14.txt") as file:
    data = file.read()

info = data.splitlines()
#print(info)

def recipieToArray(inp):
    output = [[],[]]

    reactants = inp[0:inp.index(" => ")]
    products = inp[inp.index(" => ")+4:]

    reactants = reactants.split(", ")
    for i,val in enumerate(reactants):
        reactants[i] = val.split(" ")
        reactants[i][0] = int(reactants[i][0])


    output[0] = reactants

    output[1].append(int(products[0:products.index(" ")]))
    output[1].append(products[products.index(" ")+1:])


    return output



def printRecipie(inp):
    print("Recipie: ")
    print("    Reactants:\n        ",end="")
    for reactant in inp[0]:
        print("{} {}, ".format(reactant[0], reactant[1]),end="")
    print()
    print("    Product:\n        ",end="")
    print("{} {}".format(inp[1][0], inp[1][1]))




elements = data.split(" ")
for i, val in enumerate(elements):
    if "\n" in val:
        elements[i] = elements[i][0:val.index("\n")]


for i, element in enumerate(elements):
    elements[i] = "".join(e for e in element if e.isalpha())


clean = ["ORE", "FUEL"]
for elem in elements:
    if not elem in clean:
        clean.append(elem)

clean.remove("")
print(clean)

"By now, clean is a list of all possible elements"

amounts = {}

def printAmounts():
    print("Amounts: ")
    for key, val in amounts.items():
        print("{}: {}".format(key,val))

for elem in clean:
    amounts[elem] = 0

listDict = []
colors = [Fore.LIGHTCYAN_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX,Fore.LIGHTBLUE_EX,Fore.LIGHTYELLOW_EX]

def getReactant(product):
    for recipie in listDict:
        if recipie[1][1] == product:
            return recipie[0]
    return "ORE"

def canMake(product):
    print("Trying to see if I can make",product)
    reactants = getReactant(product)
    print(reactants)
    if reactants[1] == "ORE":
        amounts["ORE"] += reactants[0]
        return True
    for reactant in reactants:
        if amounts[reactant[1]] < reactant[0]:
            return False
    return True

def make(product):
    reactants = getReactant(product)
    print(reactants)
    for reactant in reactants:
        amounts[reactant[1]] -= reactant[0]
    amounts[product] += 1

def recursiveMake(product):
    print("Recursive making", product)
    if canMake(product) == True:
        make(product)
    else:
        reactants = getReactant(product)
        for reactant in reactants:
            recursiveMake(reactant)

for i in range(len(info)):
    listDict.append(recipieToArray(info[i]))


for val in listDict:
    print(random.choice(colors),end="")
    printRecipie(val)
    print(Fore.WHITE,end="")


recursiveMake("FUEL")
printAmounts()
#print(getReactant("FUEL"))

#print(listDict)
" [       [        [ [] [    ]]]   [      ] ]"
"  Recipie Reactants #   Name      Products  "
