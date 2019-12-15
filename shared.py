

def intCode(inp, debug = 0, input3=[]):
    inpInd = 0
    list = inp.copy()
    index = 0

    output4 = []

    while(list[index]!=99):
        #print("block {}:".format(int(index/4+1)))
        if debug > 1:
            print("    {}, {}, {}, {}".format(list[index],list[index+1],list[index+2],list[index+3]))

        instruction = list[index]
        temp = instruction
        classifier = []
        classifier.append(temp%100)
        temp = int(temp/100)
        for i in range(4):
            classifier.append(temp%10)
            temp = int(temp/10)
        #print("opcode is {}".format(classifier))

        if debug > 0:
            print("    List: {}, instruction pointer: {}".format(list,index))


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
            try:
                codeInp = input3[inpInd]
                inpInd+=1
            except:
                codeInp = int(input("Enter input: "))
            list[list[index+1]] = codeInp
            index += 2
        elif(classifier[0] == 4):
            output = -1
            if classifier[1] == 1:
                output = list[index+1]
            else:
                output = list[list[index+1]]
            output4.append(output)
            #print("Output: {}".format(output))
            if(output!=0 and debug>1):
                print("    {}, {}, {}, {}".format(list[index],list[index+1],list[index+2],list[index+3]))
            index += 2
        elif(classifier[0] == 5):
            if(classifier[1] == 1):
                if(list[index+1]!=0):
                    if(classifier[2] == 1):
                        index = list[index+2]
                    else:
                        index = list[list[index+2]]
                else:
                    index += 3
            else:
                if(list[list[index+1]]!=0):
                    if(classifier[2] == 1):
                        index = list[index+2]
                    else:
                        index = list[list[index+2]]
                else:
                    index += 3

        elif(classifier[0] == 6):
            if(classifier[1] == 1):
                if(list[index+1]==0):
                    if(classifier[2] == 1):
                        index = list[index+2]
                    else:
                        index = list[list[index+2]]
                else:
                    index += 3
            else:
                if(list[list[index+1]]==0):
                    if(classifier[2] == 1):
                        index = list[index+2]
                    else:
                        index = list[list[index+2]]
                else:
                    index += 3

        elif(classifier[0] == 7):
            param = []
            for i in range(2):
                if(classifier[i+1] == 1):
                    param.append(list[index+i+1])
                else:
                    param.append(list[list[index+i+1]])
            param.append(list[index+3])

            if(param[0]<param[1]):
                list[param[2]]=1
            else:
                list[param[2]]=0
            index += 4

        elif(classifier[0] == 8):
            param = []
            for i in range(2):
                if(classifier[i+1] == 1):
                    param.append(list[index+i+1])
                else:
                    param.append(list[list[index+i+1]])
            param.append(list[index+3])
            if debug>0:
                print("        Executing 8, with param {}".format(param))
            if(param[0]==param[1]):
                list[param[2]]=1
            else:
                list[param[2]]=0
            index += 4
    return output4
