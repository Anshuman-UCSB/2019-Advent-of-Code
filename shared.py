

def intCode(list, debug = 0, input3=[], index = 0):

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

class processor:

    def __init__(self, code, pointer = 0, inp = [], out = []):
        self.code = code
        self.pointer = pointer

        self.inputs = inp
        self.inputsInd = 0
        self.outputs = out
        self.outputsInd = 0

    def __str__(self):
        return """
        Processor with following info:
                code: {}
                pointer: {}
                inputs: {}
                outputs: {}
                """.format(self.code, self.pointer, self.inputs,self.outputs)

    def isFinished(self):
        return "Fin" in self.outputs

    def process(self, prints = False):

        opcode = self.code[self.pointer]

        instructions = []

        instructions.append(opcode%100)
        opcode = int(opcode/100)
        for i in range(4):
            instructions.append(opcode%10)
            opcode = int(opcode/10)

        #instructions are opcode
        if prints:
            print(" > Using instructions {}".format(instructions))

        if(instructions[0] == 1):
            params = []
            sizeOfInstructions = 4

            for i in range(1,sizeOfInstructions-1):
                if(instructions[i] == 1):
                    params.append(self.code[self.pointer+i])
                elif(instructions[i] == 0):
                    params.append(self.code[self.code[self.pointer+i]])

            params.append(self.code[self.pointer+sizeOfInstructions-1])

            #CHANGE THIS CODE HERE#
            sum = params[0]+params[1]
            self.code[params[2]] = sum
            if prints:
                print(" + adding {} and {} and placing it at {}".format(params[0],params[1], params[2]))
                print(" () Params are {}".format(params))
            self.pointer += sizeOfInstructions
            #CODE CHANGING ENDS#

        elif(instructions[0] == 2):
            params = []
            sizeOfInstructions = 4

            for i in range(1,sizeOfInstructions-1):
                if(instructions[i] == 1):
                    params.append(self.code[self.pointer+i])
                elif(instructions[i] == 0):
                    params.append(self.code[self.code[self.pointer+i]])

            params.append(self.code[self.pointer+sizeOfInstructions-1])

            #CHANGE THIS CODE HERE#
            product = params[0]*params[1]
            self.code[params[2]] = product
            if prints:
                print(" * Multiplying {} and {} and placing it at {}".format(params[0],params[1], params[2]))
                print(" () Params are {}".format(params))
            self.pointer += sizeOfInstructions
            #CODE CHANGING ENDS#

        elif(instructions[0] == 3):
            params = []
            sizeOfInstructions = 2

            for i in range(1,sizeOfInstructions-1):
                if(instructions[i] == 1):
                    params.append(self.code[self.pointer+i])
                elif(instructions[i] == 0):
                    params.append(self.code[self.code[self.pointer+i]])

            params.append(self.code[self.pointer+sizeOfInstructions-1])

            #CHANGE THIS CODE HERE#
            inp  = -1
            try:
                inp = self.inputs[self.inputsInd]
                self.inputsInd += 1
            except:
                inp = int(input("Enter an input: "))
                self.code[params[0]] = inp
            if prints:
                print(" ^ Taking input {} and placing it at {}".format(inp, params[0]))
                print(" () Params are {}".format(params))
            self.pointer += sizeOfInstructions
            #CODE CHANGING ENDS#

        elif(instructions[0] == 4):
            params = []
            sizeOfInstructions = 2

            for i in range(1,sizeOfInstructions):
                if(instructions[i] == 1):
                    params.append(self.code[self.pointer+i])
                elif(instructions[i] == 0):
                    params.append(self.code[self.code[self.pointer+i]])


            #CHANGE THIS CODE HERE#
            out = params[0]
            if prints:
                print(" v Giving output {}.".format(out))
                print(" () Params are {}".format(params))
            self.outputs.append(out)
            self.pointer += sizeOfInstructions
            #CODE CHANGING ENDS#

        elif(instructions[0] == 5):
            params = []
            sizeOfInstructions = 3

            for i in range(1,sizeOfInstructions):
                if(instructions[i] == 1):
                    params.append(self.code[self.pointer+i])
                elif(instructions[i] == 0):
                    params.append(self.code[self.code[self.pointer+i]])

            #CHANGE THIS CODE HERE#
            if params[0] == 0:
                self.pointer += sizeOfInstructions
            else:
                self.pointer = params[1]
            if prints:
                print(" J Jumping to {}.".format(params[1]))
                print(" () Params are {}".format(params))

            #CODE CHANGING ENDS#

        elif(instructions[0] == 6):
            params = []
            sizeOfInstructions = 3

            for i in range(1,sizeOfInstructions):
                if(instructions[i] == 1):
                    params.append(self.code[self.pointer+i])
                elif(instructions[i] == 0):
                    params.append(self.code[self.code[self.pointer+i]])

            #CHANGE THIS CODE HERE#
            if params[0] != 0:
                self.pointer += sizeOfInstructions
            else:
                self.pointer = params[1]

            #CODE CHANGING ENDS#

        elif(instructions[0] == 7):
            params = []
            sizeOfInstructions = 4

            for i in range(1,sizeOfInstructions-1):
                if(instructions[i] == 1):
                    params.append(self.code[self.pointer+i])
                elif(instructions[i] == 0):
                    params.append(self.code[self.code[self.pointer+i]])
            params.append(self.code[self.pointer+sizeOfInstructions-1])


            #CHANGE THIS CODE HERE#
            if params[0] < params[1]:
                self.code[params[2]] = 1
            else:
                self.code[params[2]] = 0

            self.pointer += sizeOfInstructions
            #CODE CHANGING ENDS#

        elif(instructions[0] == 8):
            params = []
            sizeOfInstructions = 4

            for i in range(1,sizeOfInstructions-1):
                if(instructions[i] == 1):
                    params.append(self.code[self.pointer+i])
                elif(instructions[i] == 0):
                    params.append(self.code[self.code[self.pointer+i]])
            params.append(self.code[self.pointer+sizeOfInstructions-1])

            #CHANGE THIS CODE HERE#
            if params[0] == params[1]:
                self.code[params[2]] = 1
            else:
                self.code[params[2]] = 0

            self.pointer += sizeOfInstructions
            #CODE CHANGING ENDS#


        elif(instructions[0] == 99):
            if prints:
                print(" > Reached end, stopping now")
            self.outputs.append("Fin")
