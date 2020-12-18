import typing as ty
import operator as op
import re

from util import get_filename


class Node:
    idx: int = 0
    inp: str = 0
    stack: ty.List["Node"] = []
    operators: ty.Dict[str, ty.Callable] = {"+": op.add, "*": op.mul}

    left: ty.Union[int, "Node"]
    operator: ty.Callable
    right: ty.Union[int, "Node"]
    parent: ty.Union[int, "Node"]

    def __init__(self, left: ty.Optional["Node"] = None):
        if left is not None:
            self.left = left
        elif Node.inp[Node.idx] == "(":
            Node.idx += 1
            Node()
            self.left = Node.stack.pop()
        else:
            self.left = int(Node.inp[Node.idx])
            Node.idx += 1

        self.operator = Node.operators[Node.inp[Node.idx]]
        Node.idx += 1

        if Node.inp[Node.idx] == "(":
            Node.idx += 1
            Node()
            self.right = Node.stack.pop()
        else:
            self.right = int(Node.inp[Node.idx])
            Node.idx += 1

        if Node.idx < len(Node.inp):
            if Node.inp[Node.idx] == ")":
                Node.idx += 1
                Node.stack.append(self)
            elif Node.inp[Node.idx] in Node.operators:
                self.parent = Node(self)

    def solve(self):
        return self.operator(
            self.left if isinstance(self.left, int) else self.left.solve(),
            self.right if isinstance(self.right, int) else self.right.solve()
        )

    @classmethod
    def from_string(cls, inp):
        cls.idx = 0
        cls.inp = inp
        tree = cls()
        while hasattr(tree, "parent"):
            tree = tree.parent
        return tree


def part1(roots):
    return sum([root.solve() for root in roots])


class Int:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return Int(self.val * other.val)

    def __mul__(self, other):
        return Int(self.val + other.val)

    def __repr__(self):
        return str(self.val)


def part2(inp):
    solutions = []
    for line in inp:
        # replace + with * and vice versa
        line = line.replace("*", "%").replace("+", "*").replace("%", "+")
        # turn all ints (e.g. 3, 5, 8) into fake ints (e.g. Int(3), Int(5), Int(8))
        line = re.sub(r"(\d)", r"Int(\1)", line)
        solutions.append(int(str(eval(line))))
    return sum(solutions)


def main():
    with open(get_filename()) as file:
        content = file.readlines()
        inp = [Node.from_string(line.strip().replace(" ", "")) for line in content]

    print("PART 1:", part1(inp))
    print("PART 2:", part2(content))


if __name__ == '__main__':
    main()

