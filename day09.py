from util import get_filename


def step(data, start, end):
    for i in range(start, end):
        for j in range(i + 1, end):
            if data[i] == data[j]:
                continue
            if data[i] + data[j] == data[end]:
                return 0
    return data[end]


def part1(data, preamble):
    start = 0
    end = preamble

    while True:
        result = step(data, start, end)
        if result != 0:
            return result
        start += 1
        end += 1


def part2(data, invalid_num):
    for i in range(0, len(data)):
        for j in range(i + 1, len(data)):
            sub_list = data[i:j + 1]
            num = sum(sub_list)
            if num > invalid_num:
                break
            if num == invalid_num:
                return min(sub_list) + max(sub_list)


def main():
    with open(get_filename()) as file:
        inp = [int(line.strip()) for line in file]

    invalid_num = part1(inp, 25)
    print(invalid_num)
    print(part2(inp, invalid_num))


if __name__ == '__main__':
    main()
