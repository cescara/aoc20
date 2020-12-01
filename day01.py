def compare2(data):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] + data[j] == 2020:
                return data[i] * data[j]


def compare3(data):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            for k in range(j + 1, len(data)):
                if data[i] + data[j] + data[k] == 2020:
                    return data[i] * data[j] * data[k]


with open("input/day01.txt") as file:
    inp = [int(line.strip()) for line in file]
print(compare2(inp))
print(compare3(inp))
