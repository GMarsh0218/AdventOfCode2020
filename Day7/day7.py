filename = "example.txt"
# filename = "input.txt"

with open(filename) as fo:
    bags = [line.strip(".\n").replace(" bags", "").replace(" bag", "") for line in fo]

bagDict = {}
for bag in bags:
    parent, child = bag.split(" contain ")
    bagDict[parent] = child.split(", ")
    if "shiny gold" in parent:
        print(f"parent: {parent} children: {bagDict[parent]}")


# Part 1
def listContains(childBag, list):
    for string in list:
        if childBag in string:
            return True
    return False


def checkParentBag(childBag, bag_set):
    for parentBag in bagDict:
        contents = bagDict[parentBag]
        if childBag in contents or listContains(childBag, contents):
            checkParentBag(parentBag, bag_set)
            bag_set.add(parentBag)


def part1():
    bag_set = set()
    checkParentBag("shiny gold", bag_set)
    return len(bag_set)


# Part 2
def bagRT(checkBag):
    total = 0
    num, curBag = int(checkBag[:2]), checkBag[2:]
    contents = bagDict[curBag]
    if 'no other' in contents or :
        return num
    for childBag in bagDict[curBag]:
        total += num * bagRT(childBag)
    return total


def part2():
    total = 0
    for bag in bagDict["shiny gold"]:
        total += bagRT(bag)
    return total


if __name__ == '__main__':
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
