import re
import typing as ty

from util import get_filename


mask_pattern = re.compile(r"mask = (?P<mask>[01X]+)")
mem_pattern = re.compile(r"mem\[(?P<address>\d+)\] = (?P<val>\d+)")


def part1(instructions):
    mem = {}
    for instruction in instructions:
        mask = instruction[0]
        assignments = [(entry[0], list(format(entry[1], '036b'))) for entry in instruction[1:]]
        for i in range(len(mask)):
            if mask[i] == "X":
                continue
            for assignment in assignments:
                assignment[1][i] = mask[i]

        for assignment in assignments:
            mem[assignment[0]] = int("".join(assignment[1]), 2)

    return sum(mem.values())


def part2(instructions):
    mem = {}
    for instruction in instructions:
        mask = instruction[0]
        assignments = [([list(format(entry[0], '036b'))], entry[1]) for entry in instruction[1:]]
        for i in range(len(mask)):
            if mask[i] == "0":
                continue
            if mask[i] == "1":
                for assignment in assignments:
                    for address in assignment[0]:
                        address[i] = mask[i]
            else:
                for assignment in assignments:
                    buffer = []
                    for address in assignment[0]:
                        copy = list(address)
                        address[i] = "0"
                        copy[i] = "1"
                        buffer.append(copy)
                    assignment[0].extend(buffer)

        for assignment in assignments:
            for address in assignment[0]:
                mem[int("".join(address), 2)] = assignment[1]

    return sum(mem.values())


def main():
    with open(get_filename()) as file:
        instructions: ty.List[ty.List[ty.Union[str, ty.Tuple[int, int]]]] = []
        for line in file:
            if line.startswith("mask"):
                instructions.append([mask_pattern.match(line)["mask"]])
            else:
                match = mem_pattern.match(line)
                instructions[-1].append((int(match["address"]), int(match["val"])))

    print("PART 1:", part1(instructions))
    print("PART 2:", part2(instructions))


if __name__ == '__main__':
    main()

