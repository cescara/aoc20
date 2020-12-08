from util import get_filename


def parse(groups, operation):
    answers = []
    for group in groups:
        answers.append(operation(*[set(person) for person in group]))

    return sum([len(answer) for answer in answers])


def main():
    with open(get_filename()) as file:
        inp = [group.splitlines() for group in file.read().split("\n\n")]

    print(parse(inp, set.union))
    print(parse(inp, set.intersection))


if __name__ == '__main__':
    main()
