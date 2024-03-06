from collections import defaultdict, Counter

def rank(cards):
    if len(set(cards)) == 1:
        return 6
    if len(set(cards)) == 2:
        for card in set(cards):
            if cards.count(card) == 4:
                return 5
        return 4
    
    pairs = 0
    for card in set(cards):
        if cards.count(card) == 3:
            return 3
        if cards.count(card) == 2:
            pairs += 1
    
    return pairs

order = 'AKQJT98765432'

def sortCards(cards):
    cards = "".join([k*v for k, v in sorted(Counter(cards).items(), key = lambda x:order.find(x[0]) - 100 * x[1])])
    return cards 

filename = "data/input.txt"

with open(filename, 'r') as f:
    lines = f.readlines()
    dic = defaultdict(list)
    for line in lines:
        cards, bid = line.split() 
        dic[rank(cards)].append((bid, sortCards(cards)))
    
    currentRank = 1
    res = 0 
    for i in range(7):
        curr = sorted(dic[i], key = lambda cards:sorted(Counter(cards).items(), key = lambda x:10 * order.find(x[0]) * x[1]), reverse = True)
        res += sum([int(r[0]) * (currentRank + i) for (i, r) in enumerate(curr)])
        currentRank += len(curr)
        
    print("hello")
    print(res)
    


