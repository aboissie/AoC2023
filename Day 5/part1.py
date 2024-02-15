filename = "Data/input.txt"

def parseSeeds(line: str)->set:
    """
    Parses the set of seeds from the input line
    """
    return set([int(k) for k in line.split()])

def buildMapper(line:str, currentFrom: str, currentTo: str, mapper: dict)->None:
    """ 
    Build the logic for mapping for the AoC
    """
    destStart, sourceStart, rangeLength = [int(k) for k in line.strip("\n").split()]
    if currentFrom not in mapper:
        mapper[currentFrom] = {}
    if currentTo not in mapper[currentFrom]:
        mapper[currentFrom][currentTo] = []
    
    mapper[currentFrom][currentTo].append((sourceStart, destStart, rangeLength))

    return mapper 

def dfs(mapper:dict, seeds: set):
    """ 
    Extract locations from seeds
    """
    start = "seed"
    current = "seed"
    end = "location"

    locations = [k for k in seeds]
    while(current!=end):
        current = list(mapper[current].keys())[0]
        newLocs = []
        for loc in locations:
            found = False 
            for (s, d, l) in mapper[start][current]:
                if loc in range(s, s+l):
                    newLocs.append(d + loc - s)
                    found = True
                    break
            
            if not found:
                newLocs.append(loc)
                    
        locations = newLocs 
        start = current 

    return min(locations)

with open(filename, 'r') as f:
    lines = f.readlines()
    seeds = set()
    mapper = {}

    for line in lines:
        if "seeds" in line:
            proc = line.strip("\n").split("seeds:")[1]
            seeds = parseSeeds(proc)
        
        elif "to" in line:
            proc = line.strip("\n").strip("map:").strip(" ").split("-to-") 
            currentFrom = proc[0]
            currentTo = proc[1] 
        
        elif line != '\n':
            mapper = buildMapper(line, currentFrom, currentTo, mapper)

    print(dfs(mapper, seeds))
    
        