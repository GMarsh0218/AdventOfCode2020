
#  # == tree
# . == open square

with open("input.txt") as fo:
    lines = [line.splitlines() for line in fo]

print(lines)
treeMap = [[1 if c == '#' else 0 for c in line] for line in lines]

print(treeMap)
