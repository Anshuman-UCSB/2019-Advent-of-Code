

def intCode(inp):
    list = inp.copy()
    index = 0
    while(list[index]!=99):
        #print("block {}:".format(int(index/4+1)))
        #print("    {}, {}, {}, {}".format(list[index],list[index+1],list[index+2],list[index+3]))

        instruction = list[index]
        temp = instruction
        classifier = []
        classifier.append(temp%100)
        temp = int(temp/100)
        for i in range(4):
            classifier.append(temp%10)
            temp = int(temp/10)
        #print("opcode is {}".format(classifier))

        if(classifier[0] == 1):
            sum = 0
            if(classifier[1]==1):
                sum+= list[index+1]
            else:
                sum+= list[list[index+1]]
            if(classifier[2]==1):
                sum+= list[index+2]
            else:
                sum+= list[list[index+2]]
            list[list[index+3]] = sum
            index += 4
        elif(classifier[0] == 2):
            #print("Multiplying")
            product = 1
            if(classifier[1]==1):
                product*= list[index+1]
            else:
                product*= list[list[index+1]]
            if(classifier[2]==1):
                product*= list[index+2]
            else:
                product*= list[list[index+2]]
            #print("Product: {}".format(product))
            list[list[index+3]] = product
            index += 4
        elif(classifier[0] == 3):
            inp = int(input("Enter input: "))
            list[list[index+1]] = inp
            index += 2
        elif(classifier[0] == 4):
            output = -1
            if classifier[1] == 1:
                output = list[index+1]
            else:
                output = list[list[index+1]]
            print("Output: {}".format(output))
            if(output!=0):
                print("    {}, {}, {}, {}".format(list[index],list[index+1],list[index+2],list[index+3]))
            index += 2
        #print(list)
    return list
