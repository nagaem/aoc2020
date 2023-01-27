import copy


def get_occupied_seats_adjacent(layout, row, col):
    if row == 0:
        adj_rows = [0, 1]
    elif row == len(layout) - 1:
        adj_rows = [row - 1, row]
    else:
        adj_rows = [row - 1, row, row + 1]

    if col == 0:
        adj_cols = [0, 1]
    elif col == len(layout[0]) - 1:
        adj_cols = [col - 1, col]
    else:
        adj_cols = [col - 1, col, col + 1]

    occ_seats = 0
    for r in adj_rows:
        for c in adj_cols:
            # don't count this seat
            if r == row and c == col:
                continue

            if layout[r][c] == "#":
                occ_seats += 1

    return occ_seats


def get_occupied_seats_vectors(layout, row, col):
    # (x, y) pairs
    vectors = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

    if row == 0:
        vectors = [v for v in vectors if v[1] != -1]
    elif row == len(layout) - 1:
        vectors = [v for v in vectors if v[1] != 1]

    if col == 0:
        vectors = [v for v in vectors if v[0] != -1]
    elif col == len(layout[0]) - 1:
        vectors = [v for v in vectors if v[0] != 1]

    occ_seats = 0
    for v in vectors:
        total_v = [v[0], v[1]]
        seat = layout[row + v[1]][col + v[0]]

        # find first visible seat; break if no seat along vector
        while seat == ".":
            total_v[0] += v[0]
            total_v[1] += v[1]
            seat_row = row + total_v[1]
            seat_col = col + total_v[0]

            if (
                seat_row > len(layout) - 1
                or seat_row < 0
                or seat_col > len(layout[0]) - 1
                or seat_col < 0
            ):
                break

            seat = layout[seat_row][seat_col]

        if seat == "#":
            occ_seats += 1

    return occ_seats


def apply_rules(layout, max_occ, adj):
    occ_change = 0
    new_layout = copy.deepcopy(layout)
    for r, row in enumerate(new_layout):
        for c, seat in enumerate(row):
            # floor doesn't change
            if seat == ".":
                continue

            if adj:
                occ = get_occupied_seats_adjacent(layout, r, c)
            else:
                occ = get_occupied_seats_vectors(layout, r, c)

            if seat == "L" and occ == 0:
                new_layout[r][c] = "#"
                occ_change += 1
            elif seat == "#" and occ >= max_occ:
                new_layout[r][c] = "L"
                occ_change += 1

    return new_layout, occ_change


with open("./day11/input.txt") as f:
    layout = [list(row) for row in f.read().strip().split("\n")]

    # occ_change = 100
    # while occ_change != 0:
    #     occ_seats = 0
    #     layout, occ_change = apply_rules(layout, 4, True)

    # for row in layout:
    #     # print("".join(row))
    #     occ_seats += sum(map(lambda s: 1 if s == "#" else 0, row))

    # print(f"Occupied seats after stabilization (adjacent, 4 seats): {occ_seats}")

    occ_change = 100
    while occ_change != 0:
        occ_seats = 0
        layout, occ_change = apply_rules(layout, 5, False)
        # for row in layout:
        #     print("".join(row))
        # print("\n\n")

    for row in layout:
        # print("".join(row))
        occ_seats += sum(map(lambda s: 1 if s == "#" else 0, row))

    print(f"Occupied seats after stabilization (vectors, 5 seats): {occ_seats}")

