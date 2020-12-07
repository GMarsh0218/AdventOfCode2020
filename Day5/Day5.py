from statistics import median_high, median_low

with open("input.txt") as fo:
    seatdata = [line.rstrip() for line in fo]


def getSeatID(seatCode):
    rowCode = seatCode[:7]
    min, max = 0, 127
    rows = range(min, max + 1)
    for i in range(len(rowCode)):
        if len(rows) == 2:
            row = rows[1] if rowCode[i] == 'B' else rows[0]
        if rowCode[i] == 'B':  # take upper half
            min += len(rows) // 2
        else:
            max = median_low(rows)
        rows = range(min, max + 1)

    colCode = seatCode[-3:]
    min, max = 0, 7
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
