import sys
from ..lib.sockets import ClientSocket
import os
import platform
import msvcrt

def cls():
    if platform.system()in ('Linux', "Darwin"):
        os.system("clear")
    else:
        os.system("cls")

def connect() -> ClientSocket:
    client = ClientSocket(("localhost", 4040))
    client.connect()
    return client

def makeMenu(title:str="", options:tuple=tuple(), ao:int=0):
    print(title+"\n")
    for i,option in enumerate(options):
        if i==ao:print(" > "+option)
        else : print("   "+option)

def prompt(title:str="", name:str=">> ")->str:
    """
    input a variable value
    """
    print(title)
    val = input(name)
    return val

def cycle(n,a,z):
    if n < a:return z
    if n > z: return a
    return n        

def detectActionKey(logs):
    if len(logs) > 0 :
        if logs[-1] == b'\r':
            return 'enter'
        if logs[-1] == b'\x03':
            return 'exit'
    if len(logs) > 1:
        a,b = logs[-2:]
        if not (a == b'\xe0'):
            return None
        if b == b'P':
            return 'down'
        elif b == b'H':
            return 'up'
        elif b == b'K':
            return 'left'
        elif b == b'M':
            return 'right'

def askMCQ(title="", options=tuple(), header=None, footer=None)->int:
    """
        Returns the chosen option index
    """
    # title,options = q
    choice = 0
    action = None
    keyLogs=[]
    while action != 'enter':
        cls()
        if header:
            header()
        makeMenu(title, options, choice)

        if footer:
            footer()
        keyLogs.append(msvcrt.getch())
        action = detectActionKey(keyLogs)      
        if not action:
            continue
        keyLogs.clear()
        if action == 'exit':
            return sys.exit()
        elif action == 'up':
            choice = cycle(choice-1,0,len(options)-1)
        elif action == 'down':
            choice = cycle(choice+1, 0,len(options)-1)
    return choice

def goBack(callback):
    def inner(**args):
        askMCQ(title="", options=["GO BACK"], header=callback)
    return inner

if __name__ == "__main__":
    import msvcrt
    while 1:
        print(msvcrt.getch())