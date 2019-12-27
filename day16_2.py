rawInput = "80871224585914546619083218645595"
inpList = [int(s) for s in rawInput]
multiplier = 10

input = []
for i in range(multiplier):
    input.extend(inpList)
output = input.copy()
basePattern = [0,1,0,-1]
#print(input)

def iterate(input):
    #print("inp",input)
    for i in range(len(input)):
        sum = 0
        for ind, val in enumerate(input):
            sign = basePattern[int((ind+1)/(i+1))%len(basePattern)]
    #        print("Sign:",sign)
            if sign == 1:
                sum += val
            elif sign == -1:
                sum -= val
        sum = abs(sum)%10
        output[i] = sum
    #print("out",output)
    return output.copy()

def printVal():
    for val in input:
        print(val,end="")
    print()

printVal()
for i in range(100):
    input = iterate(input)
printVal()
