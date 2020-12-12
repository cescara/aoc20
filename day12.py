from util import get_filename


def solve(instructions, waypoint, part):
    dirs = {"N": 1j, "E": 1 + 0j, "S": -1j, "W": -1 + 0j}
    rotations = {"R": -1j, "L": 1j}
    ship = 0 + 0j

    for instruction in instructions:
        action, dist = instruction
        if action in dirs:
            if part == "a":
                ship += (dirs[action] * dist)
            elif part == "b":
                waypoint += (dirs[action] * dist)
        elif action in rotations:
            for _ in range(dist // 90):
                waypoint *= rotations[action]
        else:
            ship += (waypoint * dist)

    return int(abs(ship.real) + abs(ship.imag))


def main():
    with open(get_filename()) as file:
        inp = [(line[0], int(line[1:])) for line in (line.strip() for line in file)]

    print("PART 1:", solve(inp, 1 + 0j, "a"))
    print("PART 2:", solve(inp, 10 + 1j, "b"))


if __name__ == '__main__':
    main()
