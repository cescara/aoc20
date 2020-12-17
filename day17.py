from itertools import product

from util import get_filename


def get_neighbors(pos):
    factors = [[dim-1, dim, dim+1] for dim in pos]
    neighbors = set(product(*factors))
    neighbors.remove(pos)

    return neighbors


def solve(active, rounds):
    for i in range(rounds):
        new = set()
        for state in active:
            neighbors = get_neighbors(state)
            if len(neighbors & active) in [2, 3]:
                new.add(state)

            for neighbor in neighbors - active:
                if len(get_neighbors(neighbor) & active) == 3:
                    new.add(neighbor)
        active = new
    return len(active)


def main():
    with open(get_filename()) as file:
        lines = file.readlines()

    active_states_dim3 = set()
    active_states_dim4 = set()
    for x, rows in enumerate(lines):
        for y, elem in enumerate(rows):
            if elem == "#":
                active_states_dim3.add((x, y, 0))
                active_states_dim4.add((x, y, 0, 0))

    print("PART 1:", solve(active_states_dim3, 6))
    print("PART 2:", solve(active_states_dim4, 6))


if __name__ == '__main__':
    main()

