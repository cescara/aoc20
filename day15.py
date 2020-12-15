from util import get_filename


def solve(numbers, end):
    dict = {num: i + 1 for i, num in enumerate(numbers[:-1])}
    last = numbers[-1]
    for i in range(len(numbers), end):
        if last in dict:
            next = i - dict[last]
        else:
            next = 0
        dict[last] = i
        last = next
    return last


def main():
    with open(get_filename()) as file:
        inp = [int(num) for num in file.read().strip().split(",")]

    print("PART 1:", solve(inp, 2020))
    print("PART 2:", solve(inp, 30000000))


if __name__ == '__main__':
    main()

