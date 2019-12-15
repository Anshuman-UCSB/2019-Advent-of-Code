
def isValid(inp):
    list = [int(d) for d in str(inp)]

    hasRepeat = False
    last = -1
    for i in range(len(list)-1):
        if list[i]>list[i+1]:
            return False
        if list[i]==list[i+1] and not hasRepeat:
            hasRepeat = not (str(list[i])*3 in str(inp)) # part 2 solution
            #hasRepeat = True #part 1 override

    return hasRepeat

part1 = []

sum = 0
for i in range(128392, 643281):
    if(isValid(i)):
        part1.append(i)
        sum+=1
        #print("{} is a possible password".format(i))

print(sum)


exit() #not needed lol
part2 = []
check = ["000","111","222","333","444","555","666","777","888","999"]

for i in part1:
    bad = False
    for a in check:
        if a in str(i):
            bad = True
    if bad:
        print("{} is invalid.".format(i))
    if not bad:
        part2.append(i)

#print(part2)
#print(len(part2))
