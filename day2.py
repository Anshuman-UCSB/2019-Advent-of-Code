

def intCode(list):
    index = 0
    while(list[index]!=99):
        #print("block {}:".format(int(index/4+1)))
        #print("    {}, {}, {}, {}".format(list[index],list[index+1],list[index+2],list[index+3]))
        if(list[index] == 1):
            list[list[index+3]] = list[list[index+2]]+list[list[index+1]]

        elif(list[index] == 2):
            list[list[index+3]] = list[list[index+2]]*list[list[index+1]]


        index += 4
    return list

def inputIntCode(list, noun, verb):
    copy = list.copy()
    copy[1] = noun
    copy[2] = verb
    return intCode(copy)


list = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,6,19,23,1,13,23,27,1,6,27,31,1,31,10,35,1,35,6,39,1,39,13,43,2,10,43,47,1,47,6,51,2,6,51,55,1,5,55,59,2,13,59,63,2,63,9,67,1,5,67,71,2,13,71,75,1,75,5,79,1,10,79,83,2,6,83,87,2,13,87,91,1,9,91,95,1,9,95,99,2,99,9,103,1,5,103,107,2,9,107,111,1,5,111,115,1,115,2,119,1,9,119,0,99,2,0,14,0]


for i in range(100):
    for j in range(100):
        processed = inputIntCode(list, i, j)
        #print(processed[0])
        if(processed[0]==19690720):
            print(str(100*i + j))
            exit()

print("Didnt find any")
