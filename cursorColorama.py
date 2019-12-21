from colorama import *
import time

def cursor(x,y):
    return "\x1b[" + str(y) + ";"+str(x) + "H"

def moveCursor(x,y):
    print(cursor(x,y), end = "")
