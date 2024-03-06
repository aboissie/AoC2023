import re

filepath = "data/input.txt"

paths = {}
with open(filepath, "r") as f:
    instructions = [1 if i=="R" else 0 for i in f.readline().strip("\n")]
    f.readline()
    for line in f.readlines():
        for specialChar in ["(", ")", " ", "\n"]:
            line = line.replace(specialChar, "")
        from_, to_ = line.split("=")[0], line.split("=")[1].split(",")
        paths[from_] = to_

curr = 'AAA'
currInstruction = -1
numSteps = 0
while curr != "ZZZ":
    currInstruction = currInstruction + 1 if currInstruction < len(instructions) - 1 else 0
    curr = paths[curr][instructions[currInstruction]]
    numSteps += 1

print(numSteps)

    