
class processor:

    def __init__(self, codeInp):
        self.code = codeInp.copy()
        self.pointer = 0
        self.relPointer = 0
        self.inputs = []
        self.inputPtr = 0
        self.outputs = []
        self.finished = False

    def __str__(self):
        output = ""
        output += "\n     ---" + "\n"
        output += "Code: " + "\n"
        output += str(self.code[0:10]) + "..." + "\n"
        output += "\n"
        output += "Inputs:" + "\n"
        output += str(self.inputs[0:10]) + "->\n"
        output += "\n"
        output += "Outputs:" + "\n"
        output += str(self.outputs) + "          \n"
        output += "\n"
        output += "Relative pointer:" + "\n"
        output += str(self.relPointer) + "\n"
        output += "\n"
        output += "Currently at:" + "\n"
        output += "Pointer >" + str(self.pointer) + "\n"
        return output
        try:
            print(self.code[self.pointer:self.pointer+4])
        except:
            print(self.code[self.pointer])
        print()
        return("")

    def pad(self, size):
        for i in range(size):
            self.code.append(0)

    def process(self, manual = False):

        def modPtr(command, ind):
            if command[0][ind] == 2:
                command[ind] = self.relPointer + self.code[self.pointer+ind]
            elif command[0][ind] == 1:
                command[ind] = self.code[self.pointer+ind]
            elif command[0][ind] == 0:
                command[ind] = self.code[self.pointer+ind]

        command = []
        OPcode = self.code[self.pointer]
        command.append([OPcode%100])
        OPcode = int(OPcode/100)

        for i in range(4):
            command[0].append(OPcode%10)
            OPcode = int(OPcode/10)

        for i in range(1,4):
            try:
                command.append("NULL")
                if command[0][i] == 0:
                    command[i] = self.code[self.code[self.pointer+i]]
                elif command[0][i] == 1:
                    command[i] = self.code[self.pointer+i]
                elif command[0][i] == 2:
                    command[i] = self.code[self.code[self.pointer+i] + self.relPointer]
            except:
                break

        OPc = command[0][0]



        if OPc == 1:
            modPtr(command, 3)
            self.code[command[3]] = command[1] + command[2]
            self.pointer += 4

        elif OPc == 2:
            modPtr(command, 3)
            self.code[command[3]] = command[1] * command[2]
            self.pointer += 4

        elif OPc == 3:

            location = -1
            if command[0][1] == 2:
                location = self.relPointer + self.code[self.pointer+1]
            else:
                location = self.code[self.pointer+1]

            try:
                self.code[location] = self.inputs.pop(0)
                self.inputPtr += 0
                self.pointer += 2
            except:
                if manual == True:
                    inp = input(" > Enter an input\n > ")
                    self.code[location] = int(inp)
                    self.pointer += 2
                else:
                    
                    return "Waiting on input"

        elif OPc == 4:

            self.outputs.append(command[1])
            self.pointer += 2

            #print(command)
            #input(self.outputs)

        elif OPc == 5:
            if command[1] != 0:
                self.pointer = command[2]
            else:
                self.pointer += 3

        elif OPc == 6:
            if command[1] == 0:
                self.pointer = command[2]
            else:
                self.pointer += 3

        elif OPc == 7:
            modPtr(command, 3)
            if command[1] < command[2]:
                self.code[command[3]] = 1
            else:
                self.code[command[3]] = 0
            self.pointer += 4


        elif OPc == 8:
            modPtr(command, 3)
            if command[1] == command[2]:
                self.code[command[3]] = 1
            else:
                self.code[command[3]] = 0
            self.pointer += 4

        elif OPc == 9:
            self.relPointer += command[1]
            self.pointer += 2

        elif OPc == 99:
            self.finished = True

        #print(command)
