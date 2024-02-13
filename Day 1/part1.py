filename = "Day 1\Data\input.txt"

if __name__ == "__main__":
    callibrationValues = []
    with open(filename, 'rb') as f:
        lines = f.read().decode('utf-8').splitlines()
        for line in lines:
            data = [i for i in line if str.isnumeric(i)]
            callibrationValues.append(int(data[0] + data[-1]))

    sum(callibrationValues)

