with open("input.txt") as fo:
    treeMap = [[c for c in line.rstrip()] for line in fo]


def traverseMap(slope):
    pos = slope[0]
    treesHit = 0

    for i in range(slope[1], len(treeMap), slope[1]):
        row = treeMap[i]
        if row[pos] == "#":
            treesHit += 1
        pos = (pos + slope[0]) % len(row)  # adds right val to x and makes sure it doesnt go out of bounds

    return treesHit


def part2():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]  # (right, down)
    x = 1
    for slope in slopes:
        x = x * traverseMap(slope)
    return x


if __name__ == "__main__":
    print("Part 1: ", traverseMap((3, 1)))
    print("Part 2: ", part2())
