from collections import defaultdict 
from dataclasses import dataclass 

filepath = "Data/input.txt"

@dataclass 
class Gear(object):
    posX:int 
    posY:int 
    marked:bool = False 
    currentValue: int = 1 

def findSymbolPositions(lines: list):
    """ 
    Creates a dictionary of Gears with positions 
    """
    res = defaultdict(list) 
    for idx, line in enumerate(lines):
        for pos, char in enumerate(line):
            if char=="*":
                res[idx].append(Gear(posX=pos, posY=pos, marked=False, currentValue=1))

    return res 

def findNum(line: str) -> list:
    """ 
    Returns a list of tuple (number, position, length) of numbers present in line
    """
    res = []
    l = 0 
    while(l < len(line)):
        if str.isnumeric(line[l]):
            num = ""
            while(l < len(line) and str.isnumeric(line[l])):
                num += line[l]
                l += 1
            res.append((int(num), l-len(num), len(num)))
        l += 1

    return res 

def isAdjacent(idx, tuplePos, symbolPos):
    """ 
    Check if the given tuple position is adjacent to any symbol position
    """
    for pos in symbolPos:
        if abs(pos - idx) <= 1:
            for gear in symbolPos[pos]:
                if gear.posY in range(tuplePos[1] - 1, tuplePos[1] + tuplePos[2] + 1):
                    if not gear.marked:
                        gear.marked = True
                        gear.currentvalue = tuplePos[0]
                    
                    else:
                        return gear.currentvalue * tuplePos[0]
        
    return 0

with open(filepath, "r") as f:
    lines = f.readlines()
    SymbolPos = findSymbolPositions(lines)
    res = 0 
    for idx, line in enumerate(lines):
        tuplePosLine = findNum(line) 
        for tuplePos in tuplePosLine: 
            res += isAdjacent(idx, tuplePos, SymbolPos)
    
    print(res)