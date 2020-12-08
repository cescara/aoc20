from util import get_filename


def slide(data, x_step, y_step):
    trees = 0
    x = 0
    y = 0

    while x < len(data) - 1:
        x += y_step
        y += x_step
        line = data[x]

        if line[y % len(line)] == "#":
            trees += 1
    return trees


def main():
    with open(get_filename()) as file:
        inp = [line.strip() for line in file]

    print(slide(inp, 3, 1))
    print(slide(inp, 1, 1) * slide(inp, 3, 1) * slide(inp, 5, 1) * slide(inp, 7, 1) * slide(inp, 1, 2))


if __name__ == '__main__':
    main()
