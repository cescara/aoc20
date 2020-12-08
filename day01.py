from util import get_filename


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


def main():
    with open(get_filename()) as file:
        inp = [int(line.strip()) for line in file]
    print(compare2(inp))
    print(compare3(inp))


if __name__ == '__main__':
    main()
