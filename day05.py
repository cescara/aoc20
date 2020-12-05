def search(lower, upper, chars):
    if len(chars) == 0:
        return lower

    split = (upper - lower) // 2 + lower
    if chars[0] in ["F", "L"]:
        return search(lower, split, chars[1:])
    elif chars[0] in ["B", "R"]:
        return search(split + 1, upper, chars[1:])


def get_seats(data):
    seats = set()

    for line in data:
        row = search(0, 127, line[:7])
        col = search(0, 7, line[7:])
        seats.add((row * 8) + col)

    return seats


def get_missing_seat(data):
    seats = get_seats(data)
    all_seats = set(range(min(seats), max(seats)))
    return all_seats.difference(seats).pop()


with open("input/day05.txt") as file:
    inp = [line.strip() for line in file]

print(max(get_seats(inp)))
print(get_missing_seat(inp))
