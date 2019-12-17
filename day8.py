
with open("day8.txt") as file:
    data = file.read()

characters = []
for a in data:
    try:
        characters.append(int(a))
    except:
        pass

#print(characters)

class Layer:

    def __init__(self, len, height):
        self.x = len
        self.y = height
        self.grid = []
        for i in range(height):
            self.grid.append([9] * len)
        self.full = False
        self.index = 0

    def fill(self, list):
        try:
            for row in self.grid:
                for i in range(len(row)):
                    row[i] = list.pop(0)
        except:
            return -1

    def count(self, check):
        cnt = 0
        for row in self.grid:
            for val in row:
                if val == check:
                    cnt += 1
        return cnt

    def update(self):
        self.full = True
        for row in self.grid:
            if 9 in row:
                self.full = False

    def __str__(self):
        output = ""
        for row in self.grid:
            for val in row:
                output+=str(val)
            output+="\n"
        return output

layers = []

i = 0
layers.append(Layer(25,6))
layers[i].fill(characters)
layers[i].update()
print(layers[i].full)
i += 1
while layers[i-1].full == True:
    layers.append(Layer(25,6))
    layers[i].fill(characters)
    layers[i].update()
    i += 1
    #print(layers[i])
layers.pop()
print()
for i in layers:
    print(i)

count0 = []
for i in layers:
    count0.append(i.count(0))

max = min(count0)
ind = count0.index(max)

product = 1
product *= layers[ind].count(1) * layers[ind].count(2)

print(product)
