from copy import deepcopy

from util import get_filename


EMPTY = "L"
OCCUPIED = "#"
FLOOR = "."


def get_los(data, x, y, direction):
    while True:
        x += direction[0]
        y += direction[1]

        if x < 0 or y < 0 or x >= len(data) or y >= len(data[0]):
            return FLOOR
        if data[x][y] != FLOOR:
            return data[x][y]


def get_state(data, x, y, direction):
    x += direction[0]
    y += direction[1]
    if x < 0 or y < 0 or x >= len(data) or y >= len(data[0]):
        return FLOOR
    return data[x][y]


def solve(current, func, threshold):
    states = set()
    while True:
        state_hash = ''.join([item for row in current for item in row])
        if state_hash in states:
            break
        states.add(state_hash)
        new = deepcopy(current)
        for x in range(len(current)):
            for y in range(len(current[0])):
                if new[x][y] == FLOOR:
                    continue
                seats = [
                    func(current, x, y, (-1, -1)),
                    func(current, x, y, (-1, 0)),
                    func(current, x, y, (-1, 1)),
                    func(current, x, y, (0, -1)),
                    func(current, x, y, (0, 1)),
                    func(current, x, y, (1, -1)),
                    func(current, x, y, (1, 0)),
                    func(current, x, y, (1, 1)),
                ]
                occupied_seats = seats.count(OCCUPIED)

                if new[x][y] == EMPTY and occupied_seats == 0:
                    new[x][y] = OCCUPIED
                elif new[x][y] == OCCUPIED and occupied_seats >= threshold:
                    new[x][y] = EMPTY
        current = new
    return sum([row.count(OCCUPIED) for row in current])


def main():
    with open(get_filename()) as file:
        inp = [list(line.strip()) for line in file]

    print("PART 1:", solve(inp, get_state, 4))
    print("PART 2:", solve(inp, get_los, 5))


if __name__ == '__main__':
    main()
