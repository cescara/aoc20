from util import get_filename


def part1(adapters):
    jolts_1 = 0
    jolts_3 = 0

    for i in range(0, len(adapters)):
        if i == len(adapters) - 1:
            continue

        jolts = adapters[i + 1] - adapters[i]
        if jolts == 1:
            jolts_1 += 1
        elif jolts == 3:
            jolts_3 += 1
    return jolts_1 * jolts_3


def part2(adapters):
    jolts = [1]
    for i in range(1, len(adapters)):
        jolts.append(adapters[i] - adapters[i - 1])

    paths = {0: 1}
    for i in adapters[1:]:
        paths[i] = paths.get(i - 1, 0) + paths.get(i - 2, 0) + paths.get(i - 3, 0)

    return paths[adapters[-1]]


def main():
    with open(get_filename()) as file:
        inp = sorted([int(line.strip()) for line in file])
        inp = [0, *inp, inp[-1] + 3]

    print(part1(inp))
    print(part2(inp))


if __name__ == '__main__':
    main()
