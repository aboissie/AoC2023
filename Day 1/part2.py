filename = "Data\input.txt"

numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

def findNumbers(line: str)->int:
    """
    Parses the input string and returns the number found in it.
    """
    posMap = {}
    for number in numbers:
        if number in line: 
            prev = -1
            while line.find(number, prev + 1) != -1:
                prev = line.find(number, prev + 1)
                posMap[prev] = numbers[number]
    
    for idx, num in enumerate(line):
        if str.isnumeric(num):
            posMap[idx] = str(num)
    
    return int(posMap[min(posMap)] + posMap[max(posMap)])

if __name__ == "__main__":
    res = 0
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip("\n")

            print(findNumbers(line))
            res += findNumbers(line)

    print(res)

