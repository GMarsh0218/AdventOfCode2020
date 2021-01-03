with open("input.txt") as fo: fileText = [line.rstrip() for line in fo]
data = []
group = ""
members = 0

for i in range(len(fileText)):
    line = fileText[i]
    if i + 1 == len(fileText):
        group += line
        members += 1
        data.append((group, members))
        break
    if line == "":
        data.append((group, members))
        group = ""
        members = 0
    else:
        group += line
        members += 1


def part1():
    x = 0
    for grp in data:
        x += len(set(grp[0]))
    return x


def part2():
    x = 0
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    for grp in data:
        for letter in lowercase:
            if grp[0].count(letter) == grp[1]:
                x += 1
    return x


if __name__ == '__main__':
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
