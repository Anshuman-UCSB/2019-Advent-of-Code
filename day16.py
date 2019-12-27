from cursorColorama import *

basePattern = [0, 1, 0, -1]
inputSignal = 80871224585914546619083218645595

inputSignal = str(inputSignal) * 1
inputSignal = int(inputSignal)

inputSignal = [int(d) for d in str(inputSignal)]


def phase(input):
    output = []
    for i in range(len(input)):
        sum = 0
        ind = 1
        for val in input:
            sum+=val*basePattern[int((ind)/(i+1))%len(basePattern)]
            sum = sum%10
            ind+=1
        output.append(int(str(sum)[-1]))
    return output.copy()

temp = inputSignal
for i in range(101):
if i%100 ==0:
        print("Iteration {},".format(i),temp)
    temp = phase(temp)
