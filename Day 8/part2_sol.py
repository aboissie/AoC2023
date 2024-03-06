import math

filepath = "data/input2.txt"

paths = {}
with open(filepath, "r") as f:
    instructions = [1 if i=="R" else 0 for i in f.readline().strip("\n")]
    f.readline()
    for line in f.readlines():
        for specialChar in ["(", ")", " ", "\n"]:
            line = line.replace(specialChar, "")
        from_, to_ = line.split("=")[0], line.split("=")[1].split(",")
        paths[from_] = to_

def checkFinished(current):
    return all([k[-1] == "Z" for k in current])

def oneStep(current, currInstruction):
    for i, k in enumerate(current):
        current[i] = paths[k][instructions[currInstruction]]
    return current 

currents = [key for key in paths.keys() if key[-1] == "A"]
currInstruction = -1
numSteps = 0
y = -1
while(not checkFinished(currents)):
    currInstruction = currInstruction + 1 if currInstruction < len(instructions) - 1 else 0
    currents = oneStep(currents, currInstruction)
    numSteps += 1

    for i, k in enumerate(currents):
        if k[-1] == "Z":
            y = math.lcm(numSteps, y) if y!=-1 else numSteps
    
    currents = [k for k in currents if k[-1]!="Z"]

print(y)
    