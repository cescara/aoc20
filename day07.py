import re
import typing as tp

from util import get_filename

parent_pattern = re.compile(r"(?P<parent>.+) bags contain (?P<contents>.+)")
child_pattern = re.compile(r"(?P<amount>\d+) (?P<colors>.+?) bags?")


class Bag:
    def __init__(self, name: str):
        self.name = name
        self.children: tp.Dict[Bag, int] = {}
        self.parents: tp.Dict[Bag, int] = {}

    def __str__(self):
        return f"Bag({self.name})"


def parse(data) -> tp.Dict[str, Bag]:
    bags = {}
    for line in data:
        match = parent_pattern.match(line)
        parent_name = match["parent"]

        if parent_name not in bags:
            bags[parent_name] = Bag(parent_name)
        parent = bags[parent_name]

        if match["contents"] == "no other bags.":
            continue

        children = child_pattern.finditer(match["contents"])
        for match in children:
            child_name = match["colors"]
            if child_name not in bags:
                bags[child_name] = Bag(child_name)
            child = bags[child_name]

            parent.children[child] = int(match["amount"])
            child.parents[parent] = int(match["amount"])

    return bags


def get_parents(bag):
    for parent in bag.parents:
        yield from get_parents(parent)
    yield {parent.name for parent in bag.parents}


def get_child_amounts(bag, amount=0):
    for child, child_amount in bag.children.items():
        amount += child_amount * sum(get_child_amounts(child, 1))
    yield amount


def part1(bag_name, bags):
    return len(set.union(*get_parents(bags[bag_name])))


def part2(bag_name, bags):
    return sum(get_child_amounts(bags[bag_name]))


def main():
    with open(get_filename()) as file:
        inp = [line.strip() for line in file]

    print(part1("shiny gold", parse(inp)))
    print(part2("shiny gold", parse(inp)))


if __name__ == '__main__':
    main()
