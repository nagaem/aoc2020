def parsePass(bPass):
    splits = {"F": 1, "B": -1, "L": 1, "R": -1}
    row = list(range(128))
    col = list(range(8))

    # Get front/back location
    for c in bPass[0:7]:
        idx = int(len(row) / 2)
        row = row[idx:] if splits[c] < 0 else row[:idx]

    for c in bPass[7:]:
        idx = int(len(col) / 2)
        col = col[idx:] if splits[c] < 0 else col[:idx]

    return row[0], col[0]


def findSeat(s_ids):
    s_ids.sort()
    for s in range(0, len(s_ids) - 1):
        if s_ids[s + 1] - s_ids[s] == 2:
            return s_ids[s] + 1


if __name__ == "__main__":
    s_ids = []
    with open("./day5/input.txt") as f:
        for line in f:
            row, col = parsePass(line.strip())
            s_ids.append(row * 8 + col)

    print(f"Max seat id: {max(s_ids)}")
    print(findSeat(s_ids))