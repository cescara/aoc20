import re
import typing as ty
from functools import reduce

from util import get_filename


range_pattern = re.compile(r"(?P<name>.+): (?P<first_1>\d+)-(?P<first_2>\d+) or (?P<second_1>\d+)-(?P<second_2>\d+)")


class Field:
    def __init__(self, inp: str):
        match = range_pattern.match(inp)
        self.name: str = match["name"]
        self.ranges: ty.Tuple[ty.Iterable[int], ty.Iterable[int]] = (
            range(int(match["first_1"]), int(match["first_2"]) + 1),
            range(int(match["second_1"]), int(match["second_2"]) + 1))

    def in_range(self, value):
        return value in self.ranges[0] or value in self.ranges[1]


class Ticket:
    def __init__(self, inp: str, fields: ty.List[Field]):
        self.values: ty.List[ty.Tuple[int, bool]] = [(int(value), False) for value in inp.split(",") if value]
        self.fields = fields
        self.valid: bool = self.validate()

    def validate(self):
        for i, (value, _) in enumerate(self.values):
            result = len(self.fields) * [False]
            for j in range(len(self.fields)):
                result[j] = self.fields[j].in_range(value)
            if any(result):
                self.values[i] = (value, True)
        return all([valid for _, valid in self.values])

    def invalid_sum(self):
        return sum([value for value, valid in self.values if not valid])


def part1(tickets: ty.List[Ticket]):
    return sum([ticket.invalid_sum() for ticket in tickets if not ticket.valid])


def part2(my_ticket: Ticket, tickets: ty.List[Ticket]):
    remaining = {field for field in my_ticket.fields}
    cols = {field[0]: set() for field in enumerate(my_ticket.values)}
    while not all(len(v) == 1 for v in cols.values()):
        for i in range(len(my_ticket.values)):
            if len(cols[i]) == 1:
                continue
            possible = set(remaining)
            for ticket in tickets:
                value = ticket.values[i][0]
                for field in remaining:
                    if field not in possible:
                        continue
                    if not field.in_range(value):
                        possible.discard(field)
            cols[i] = possible
            if len(possible) == 1:
                remaining.discard(next(iter(possible)))

    idcs = [key for key, value in cols.items() if list(value)[0].name.startswith("departure")]

    return reduce(int.__mul__, [value for i, (value, _) in enumerate(my_ticket.values) if i in idcs])


def main():
    with open(get_filename()) as file:
        parts = file.read().split("\n\n")

    fields = [Field(field) for field in parts[0].split("\n")]
    my_ticket = Ticket(parts[1].split("\n")[1], fields)
    tickets = [Ticket(ticket, fields) for ticket in parts[2].split("\n")[1:] if ticket]

    print("PART 1:", part1(tickets))
    print("PART 2:", part2(my_ticket, [ticket for ticket in tickets if ticket.valid]))


if __name__ == '__main__':
    main()

