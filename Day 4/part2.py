from collections import Counter 

filename = "Data/input.txt"
scores = {}

def parse(line: str)->None:
    """
    Parses the input proc and gives the scores for the card 
    """
    cardNumber = int(line.split(':')[0].split("Card")[1])
    proc = line.strip("\n").split(":")[1].split("|")
    set1 = Counter([int(k) for k in proc[0].split(" ") if str.isnumeric(k)])
    set2 = Counter([int(k) for k in proc[1].split(" ") if str.isnumeric(k)])

    currentMax = 0
    for k in set(set1).intersection(set(set2)):
        currentMax += min(set1[k], set2[k])
    
    scores[cardNumber] = currentMax

def countScore():
    """
    Counts the score for the game
    """
    res = 0
    dic = {k: 1 for k in scores}
    for k in scores:
        for i in range(k + 1, k + 1 + scores[k]):
            dic[i] += dic[k]
        res += dic.get(k, 1) 
    
    return res 

with open(filename, 'r') as f:
    lines = f.readlines()
    res = 0
    for line in lines:
        parse(line)
    
    print(countScore())

    print(res)
