"Assuming already got valid maze"
from cursorColorama import *

with open("day15maze.txt") as file:
    maze = eval(file.read())

visited = []
finalPath = []
startCoord = [21,21]

def hasCoord(coord, list):
    #coord = [x,y]
    for val in list:
        if val[0] == coord[0] and val[1] == coord[1]:
            return True
            return False

def printMaze():
    moveCursor(0,0)
    translate = ["░","█","▓","O"]
    colors = [Fore.WHITE, Fore.RED, Fore.LIGHTBLUE_EX, Fore.BLUE, Fore.GREEN]
    for y, row in enumerate(maze):
        for x,val in enumerate(row):
            if val == 1:
                print(colors[0]+translate[1],end="")
            elif val == 0:
                if hasCoord([x,y], finalPath):
                    print(colors[2]+translate[1],end="")
                elif hasCoord([x,y], visited):
                    print(colors[1]+translate[1],end="")
                else:
                    print(Fore.BLACK+translate[1],end="")
            elif val == 3:
                print(colors[3]+translate[1],end="")
            elif val == 2:
                startCoord = [x,y]
                #print("Defining startCoord",startCoord)
                print(colors[4]+translate[1],end="")
            print(Fore.WHITE,end="")
        print()

bots = []
class Bot:
    def __init__(self, parent, inpCoord=[0,0]):
        self.parent = parent
        self.coord = inpCoord
        self.visited = visited
        self.validMoves = []
        try:
            self.path = parent.path.copy()
        except:
            self.path = []
        self.path.append(self.coord.copy())
        self.updateValids()
        self.bday = True
        self.dead = False
        self.foundOxy = False

    def __str__(self):
        output = "Bot at {}, with {} valids.".format(self.coord,len(self.validMoves))
        return output

    def update(self):
        if self.dead:
            return
        if not hasCoord(self.coord,  self.visited):
            self.visited.append(self.coord.copy())
        if self.bday == True:
            self.bday = False
            return ":)"
        self.updateValids()
        if len(self.validMoves) == 1:
            self.moveTo(self.validMoves[0])
        if len(self.validMoves) > 1:
            self.moveTo(self.validMoves.pop())
            for move in self.validMoves:
                bots.append(Bot(self,inpCoord = move))

    def moveTo(self, pos):
        if not pos in self.visited:
            self.visited.append(pos)
        self.coord = pos.copy()
        self.path.append(self.coord.copy())

    def updateValids(self):
        possibles = []
        for i in range(4):
            possibles.append(self.coord.copy())
        possibles[0][1]-=1
        possibles[1][0]+=1
        possibles[2][1]+=1
        possibles[3][0]-=1
        #print(possibles)
        #print(possibles)
        for ind, val in enumerate(possibles):
            #print(val, maze[val[1]][val[0]])

            if maze[val[1]][val[0]] == 3:
                self.foundOxy = True
                possibles = [[val[1], val[0]]]
                break

            if maze[val[1]][val[0]] == 1 or hasCoord(val, visited):
                #print("val is getting removed",val)
                possibles[ind] = "NULL"
                #print("Remaining",possibles)
        try:
            while True:
                possibles.remove("NULL")
        except:
            self.validMoves = possibles.copy()
        if len(self.validMoves) == 0:
            self.dead = True





bots.append(Bot("NULL", inpCoord = startCoord))
alive = True

frame, skipframe = 0,10
done = False
while alive and not done:
    alive = False
    for bot in bots:
        if done == True:
            break
        if bot.dead == False:
            alive = True
        bot.update()
        if bot.foundOxy == True:
            finalPath = bot.path.copy()
            done = True
    if frame % skipframe == 0:
        printMaze()
    frame+=1

printMaze()

print(len(finalPath))
input()
    #input(str(bot))

"242 too high, answer for someone else?"
"237 too low"
"238 lmao"
