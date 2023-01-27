from functools import reduce

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


def count_trees(f):
    trees = [0] * len(slopes)
    line_length = 0
    for i, line in enumerate(f.readlines()):
        # We start on line 0, posn 0 so check the line length then skip it
        if i == 0:
            line_length = len(line.strip())
            continue

        for slope_idx, incs in enumerate(slopes):
            r_inc, d_inc = incs

            # In cases where the slope has us skipping lines
            if i % d_inc != 0:
                continue

            # Where in the repeating pattern are we?
            idx = int(((r_inc * i) / d_inc) % line_length)

            # Is the char at this index a tree?
            if line[idx] == "#":
                trees[slope_idx] += 1

    return trees


if __name__ == "__main__":
    trees = 1
    with open("./day3/input.txt") as f:
        print(reduce(lambda a, b: a * b, count_trees(f)))
