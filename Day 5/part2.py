filename = "Data/input.txt"

def parseSeeds(line: str) -> set:
    """
    Parses the set of seeds from the input line
    """
    seeds = set()
    proc = [int(k) for k in line.split()]
    for k in range(len(proc)//2):
        for i in range(proc[2 * k + 1]):
            seeds.add(proc[2 * k] + i)

    return seeds

def buildMapper(line: str, currentFrom: str, currentTo: str, mapper: dict) -> None:
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

def precomputeDestinations(mapper: dict) -> dict:
    """
    Precompute destination locations for each source location
    """
    destinations = {}
    for sourceFrom in mapper:
        for sourceTo in mapper[sourceFrom]:
            for (sourceStart, destStart, rangeLength) in mapper[sourceFrom][sourceTo]:
                for loc in range(sourceStart, sourceStart + rangeLength):
                    destinations[(sourceFrom, loc)] = destStart + loc - sourceStart

    return destinations

def dfs(destinations: dict, seeds: set) -> int:
    """ 
    Extract locations from seeds
    """
    current = ("seed",)
    end = ("location",)

    locations = seeds
    while current != end:
        current = list(destinations[current].keys())[0]
        locations = {destinations[current][(current[0], loc)] for loc in locations if (current[0], loc) in destinations[current]}

    return min(locations)

with open(filename, 'r') as f:
    lines = f.readlines()
    seeds = set()
    mapper = {}

    print("PROC")
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

    print("DONE MAPPING")
    destinations = precomputeDestinations(mapper)
    print(dfs(destinations, seeds))
