with open("day14.txt") as file:
    data = file.read().splitlines()

for dat in data:
    print(dat)

print()

recipies = []


def lineToRecipie(line):
    split = line.split(" => ")
    left = split[0]
    right = split[1]

    right = right.split(" ")
    right[0] = int(right[0])

    left = left.split(", ")
    for i in range(len(left)):
        left[i] = left[i].split(" ")
        left[i][0] = int(left[i][0])

    return [left,right]


for dat in data:
    recipies.append(lineToRecipie(dat))



def getRecipie(prod):
    for recip in recipies:
        if recip[1][1] == prod:
            return recip
    return "ORE"

counts = {}

def initializeCounts():
    counts["ORE"] = 0
    for recip in recipies:
        counts[recip[1][1]] = 0

def make(prod, count):

    recip = getRecipie(prod)


    "count is how many needed"
    "min is how many needed to actually make"
    "batch is how many per batch"

    batch = recip[1][0]
    min = count-1
    min -= min%batch
    #print("          Starting min",min)
    while min<count:
        min+= batch
    #print("          Found min",min)
    min = int(min/batch)

    #print("    Making",min,"of",prod)
    counts[prod] += min*batch
    for react in recip[0]:
        counts[react[1]]-=react[0]*min
    makeChild()

def makeChild():
    valid = False
    while not valid:
        valid = True
        for key, val in counts.items():
            #print("        Checking [{}] : {}".format(key,val))
            if key != "ORE" and val < 0:
                make(key, abs(val))
                valid = False
                break



low, high = 1, 10**13
for i in range(100):
    mid = int((low+high)/2)
    initializeCounts()
    print("H{}, L{}, M{}".format(high,low,mid))
    print("Making FUEL:",mid)
    make("FUEL",mid)
    print(counts)
    print()
    print("Needs {} Ore.".format(abs(counts["ORE"])))
    delta = 10**12+counts["ORE"]
    print("Delta 1tril is",delta)
    if delta > 0:
        low = mid+1
        print("Shifting range up")
    elif delta<0:
        high = mid-1
        print("Shifting range down")

"2169535"
