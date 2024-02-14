from collections import Counter 

filename = "Data/input.txt"

with open(filename, 'r') as f:
    lines = f.readlines()
    res = 0
    for line in lines:
        proc = line.strip("\n").split(":")[1].split("|")
        set1 = Counter([int(k) for k in proc[0].split(" ") if str.isnumeric(k)])
        set2 = Counter([int(k) for k in proc[1].split(" ") if str.isnumeric(k)])

        currentMax = 0
        for k in set(set1).intersection(set(set2)):
            currentMax += min(set1[k], set2[k])
        
        res += int(2 ** (currentMax - 1))

    print(res)
