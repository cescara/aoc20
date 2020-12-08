import re
from typing import List, Set, Tuple

from util import get_filename

pattern = re.compile(r"(?P<op>.+) (?P<value>[-+]\d+)")


class Computer:
    def __init__(self, data, mode="naive"):
        self.boot_code: List[Tuple[str, int]] = []
        for line in data:
            match = pattern.match(line)
            self.boot_code.append((match["op"], int(match["value"])))
        self.acc: int = 0
        self.ptr: int = 0
        self.safe_state: Tuple[int, int, Set[int]] = (0, 0, set())
        self.debug: bool = False
        self.mode: str = mode
        self.executed: Set[int] = set()
        self.switched: Set[int] = set()

    def run(self):
        while True:
            if self.ptr in self.executed:
                if self.mode != "debug":
                    break
                self.acc, self.ptr, self.executed = self.safe_state
                self.debug = False
            if self.ptr == len(self.boot_code):
                break

            op, value = self.boot_code[self.ptr]
            if (op == "nop" or op == "jmp") and \
                    self.ptr not in self.switched and self.debug is False and self.mode == "debug":
                self.safe_state = self.acc, self.ptr, set(self.executed)
                self.switched.add(self.ptr)
                self.debug = True
                if op == "nop":
                    op = "jmp"
                else:
                    op = "nop"
            self.executed.add(self.ptr)

            if op == "acc":
                self.acc += value
                self.ptr += 1
            elif op == "nop":
                self.ptr += 1
            elif op == "jmp":
                self.ptr += value

        return self.acc


def main():
    with open(get_filename()) as file:
        inp = [line.strip() for line in file]

    print(Computer(inp).run())
    print(Computer(inp, "debug").run())


if __name__ == '__main__':
    main()
