import re

from util import get_filename

pattern = re.compile(r"(?P<first>\d+)-(?P<second>\d+) (?P<pattern>[a-z]): (?P<password>\w+)")


def parse(match):
    return {"first": int(match.group("first")), "second": int(match.group("second")), "pattern": match.group("pattern"),
            "password": match.group("password")}


def part1(data):
    valid = 0
    for elem in data:
        count = elem["password"].count(elem["pattern"])
        if elem["first"] <= count <= elem["second"]:
            valid += 1
    return valid


def part2(data):
    valid = 0
    for elem in data:
        char = elem["pattern"]
        password = elem["password"]
        if (password[elem["first"] - 1] == char) != (password[elem["second"] - 1] == char):
            valid += 1
    return valid


def main():
    with open(get_filename()) as file:
        inp = [parse((pattern.match(line))) for line in file]
    print(part1(inp))
    print(part2(inp))


if __name__ == '__main__':
    main()
