from util import get_filename


class Search:
    def __init__(self, adapters):
        self.adapters = adapters
        self.chains = []
        self.chain_count = 0

    def run(self, i, chain):
        j = 1
        while True:
            if i + j >= len(self.adapters):
                if chain[-1] == self.adapters[-1]:
                    self.chains.append(chain)
                break
            elif self.adapters[i + j] - self.adapters[i] > 3:
                break
            else:
                new_chain = list(chain)
                new_chain.append(self.adapters[i + j])
                self.run(i + j, new_chain)
            j += 1
        return len(self.chains)

    def run2(self, i, chain):
        j = 1
        while True:
            if i + j >= len(self.adapters):
                if chain[-1] == self.adapters[-1]:
                    #self.chains.append(list(chain))
                    self.chain_count += 1
                break
            elif self.adapters[i + j] - self.adapters[i] > 3:
                break
            else:
                if i < len(chain):
                    chain = chain[:i]
                chain.append(self.adapters[i + j])
                self.run2(i + j, chain)
            j += 1


def part1(adapters):
    jolts_1 = 0
    jolts_3 = 0

    for i in range(0, len(adapters)):
        if i == len(adapters) - 1:
            continue

        jolts = adapters[i + 1] - adapters[i]
        if jolts == 1:
            jolts_1 += 1
        elif jolts == 3:
            jolts_3 += 1
    return jolts_1 * jolts_3


def traverse(i, adapters, chain):
    j = 1
    while True:
        if i + j >= len(adapters):
            yield chain
        elif adapters[i + j] - adapters[i] > 3:
            break
        else:
            chain.append(adapters[i + j])
            traverse(i + j, adapters, chain)
        j += 1


def part2(adapters):
    # jolts = []
    # for i in range(0, len(adapters) - 1):
    #     jolts.append(adapters[i + 1] - adapters[i])
    # ad = dict(adapters)
    # nums = [*range(0, adapters[-1])]
    # jolts = [0] * adapters[-1]
    # jolts[0] = 1
    # for i in range(0, len(nums)):
    #     diffs[i] = ad.get(nums[i - 1], 0) + ad.get(nums[i - 2], 0) + ad.get(nums[i - 3], 0)
    # ad = {adapter: 1 for adapter in adapters}
    # nums = [*range(0, adapters[-1])]
    # jolts = {0: 1}
    # for i in adapters:
    #     if i == 0:
    #         continue
    #     # if i == 0:
    #     #     diffs[i] = 1
    #     #     continue
    #     # if i in ad:
    #     jolts[i] = jolts.get(i - 1, 0) + jolts.get(i - 2, 0) + jolts.get(i - 3, 0)
    # else:
    #     jolts[i] = 0

    jolts = []
    for i in range(len(adapters)):
        if i == 0:
            jolts.append(1)
            continue
        jolts.append(adapters[i] - adapters[i - 1])

    perms = {0: 1}
    for i in adapters[1:]:
        perms[i] = perms.get(i - 1, 0) + perms.get(i - 2, 0) + perms.get(i - 3, 0)

    print(adapters)
    print(jolts)
    print(perms)
    return perms[adapters[-1]]


# def part2(adapters):
#     all_paths = 1
#     i = 1
#     while True:
#         if i >= len(adapters) - 1:
#             break
#     #for i in range(1, len(adapters)):
#         paths = 0
#         x = adapters[i]
#         for j in range(i + 1, len(adapters)):
#             y = adapters[j]
#             if y - x <= 3:
#                 paths += 1
#             else:
#                 break
#             i = j
#         if paths == 3:
#             paths = 4
#         all_paths *= paths
#
#     print(all_paths)

    # search = Search(adapters)
    # search.run2(0, [0])
    # # for chain in search.chains:
    # #     print(chain)
    # return search.chain_count // 2


def main():
    #with open("input/sample.txt") as file:
    with open(get_filename()) as file:
        inp = sorted([int(line.strip()) for line in file])
        inp = [0, *inp, inp[-1] + 3]

    print(part1(inp))
    print(part2(inp))


if __name__ == '__main__':
    main()
