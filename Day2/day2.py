with open("input.txt") as fo:
    passwords = [line.rstrip() for line in fo]

part1 = 0
part2 = 0

for line in passwords:
    minCharCount = int(line[0:line.find('-')])
    maxCharCount = int(line[line.find('-') + 1:line.find(' ')])
    passChar = line[line.find(' ') + 1]
    password = line[line.find(' ')+4:]
    passCharCount = password.count(passChar)
    if minCharCount <= passCharCount <= maxCharCount:
        part1 += 1
    if (password[minCharCount-1] == passChar) ^ (password[maxCharCount - 1] == passChar):
        part2 += 1

print("Part1:", part1)
print("Part2:", part2)
