import regex as re

from util import get_filename


def parse_rule(inp):
    parts = inp.split("|")
    if parts[0].startswith(" \""):
        return inp[2]
    return [list(map(int, part.strip().split(" "))) for part in parts]


pattern = ""


def lookup(idx, rules):
    global pattern
    rule = rules[idx]
    if isinstance(rule, str):
        pattern += rule
        return

    if len(rule) == 1:
        for option in rule:
            for char in option:
                lookup(char, rules)
    else:
        pattern += "("
        if idx not in rule[1]:
            for char in rule[0]:
                lookup(char, rules)
            pattern += "|"
            for char in rule[1]:
                lookup(char, rules)
        else:
            pattern += "("
            if len(rule[1]) == 2:
                lookup(rule[1][0], rules)
                pattern += ")+"
            else:
                current_group = pattern.count('(') - 1
                lookup(rule[1][0], rules)
                pattern += f")(?{current_group})?("
                lookup(rule[1][2], rules)
                pattern += ")"
        pattern += ")"


def solve(rules, messages):
    global pattern
    valid = []
    lookup(0, rules)
    regex = re.compile(pattern)
    for message in messages:
        if regex.fullmatch(message):
            valid.append(message)
    return len(valid)


def main():
    global pattern
    with open(get_filename()) as file:
        content = file.read().split("\n\n")
    rules = {int(index): parse_rule(rule) for index, rule in map(lambda r: r.split(":"), content[0].split("\n"))}
    messages = [message for message in content[1].split("\n")]

    print("PART 1:", solve(rules, messages))
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    pattern = ""
    print("PART 2:", solve(rules, messages))


if __name__ == '__main__':
    main()




