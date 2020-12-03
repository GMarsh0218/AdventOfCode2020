
with open("input.txt") as fo:
    input = [int(line) for line in fo]

x = len(input)

for i in input:
    for j in input:
        if i + j == 2020:
            print("Part1: " , i*j)

# part 2

