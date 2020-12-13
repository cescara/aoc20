from util import get_filename


def part1(start, busses):
    best = 0
    earliest = float("inf")
    for bus in busses:
        if bus is None:
            continue

        departure = bus
        while True:
            if departure >= start:
                if departure < earliest:
                    best = bus
                    earliest = departure
                break
            departure += bus

    return (earliest - start) * best


def part2(busses):
    offset = 0
    earliest = step = busses[0]
    for bus in busses[1:]:
        offset += 1
        if bus is None:
            continue
        while True:
            if (earliest + offset) % bus == 0:
                step *= bus
                break
            earliest += step
    return earliest


def main():
    with open(get_filename()) as file:
        inp = file.readlines()
        entries = [int(entry) if entry != "x" else None for entry in inp[1].split(",")]

    print("PART 1:", part1(int(inp[0]), entries))
    print("PART 2:", part2(entries))


if __name__ == '__main__':
    main()

