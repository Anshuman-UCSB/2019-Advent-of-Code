from colorama import *
import time

def pos(x,y):
    return "\x1b[" + str(y) + ";"+str(x) + "H"

word = "Loading.........."
i = 0

print(Fore.RED)
print(pos(30,5) + "This is in a different")



while True:
    time.sleep(.05)
    print(pos(0,0)+word[0:i%len(word)]+"  ")
    print("test", [...])
    i+=1
