

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
