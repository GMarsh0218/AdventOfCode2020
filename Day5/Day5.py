from statistics import median_low

with open("input.txt") as fo:
    seatdata = [line.rstrip() for line in fo]

def bsp(code, min, max):
    chars = range(min, max+1)
    for i in range(len(code)):
        if len(chars) == 2:
            return chars[1] if code[i] == 'B' else chars[0]
        if code[i] == 'B':  # take upper half
            min += len(chars) // 2
        else:
            max = median_low(chars)
        chars = range(min, max + 1)


def getSeatID(seatCode):
    rowCode, colCode = seatCode[:7] ,seatCode[-3:]
    row = (rowCode, 0, 127)


    cols = range(min, max + 1)
    for i in range(len(colCode)):
        if len(cols) == 2:
            col = cols[1] if colCode[i] == 'R' else cols[0]
        if colCode[i] == 'R':  # take upper half
            min += len(cols) // 2
        else:
            max = median_low(cols)
        cols = range(min, max + 1)
    seatID = row * 8 + col
    return row * 8 + col


def part1():
    seatIDS = [getSeatID(x) for x in seatdata]
    return max(seatIDS)


def part2():
    seatIDS = sorted([getSeatID(x) for x in seatdata])
    for i in range(1, len(seatIDS) - 2):
        if seatIDS[i] + 2 == seatIDS[i+1]:
            return seatIDS[i]+1


if __name__ == "__main__":
    print("Day 5")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
