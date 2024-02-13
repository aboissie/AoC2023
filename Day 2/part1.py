from typing import Union 

filename = "Data\input.txt"

redCubes = 12
greenCubes = 13
blueCubes = 14

limits = {"red": redCubes, "green": greenCubes, "blue": blueCubes}

def parseLine(line:str):
    """
    Determines if the line is valid
    """
    currentMax = {}
    for color in ["red", "green", "blue"]:
        prev = -1
        counter = 0
        while(line.find(color, prev + 1) != -1):
            prev = line.find(color, prev + 1) 
            counter = int(line[prev - 3:prev-1])
            currentMax[color] = max(counter, currentMax.get(color, 0))

    return int(line[5:8].strip(": ").strip(":")), currentMax
                  
def powerSet(dic:dict)->int:
    """
    Returns the power of a set of cubes
    """
    res = 1
    for key in dic:
        res *= dic[key]
    return res

if __name__ == "__main__":
    res = 0
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        for line in lines: 
            _, currentMax =  parseLine(line)
            res += powerSet(currentMax)

    print(res)

