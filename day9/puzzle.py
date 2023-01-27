def canSum(candidates, target):
    # very similar to day1
    candidates.sort()
    for c1 in candidates:
        c2_idx = len(candidates) - 1
        while (total := c1 + candidates[c2_idx]) > target:
            c2_idx -= 1
            if c2_idx < 0:
                break

        if c1 == candidates[c2_idx]:
            continue

        if total == target:
            return True

    return False


def findInvalid(numbers, preamble):
    for i, n in enumerate(numbers[preamble:]):
        sum_candidates = numbers[i : i + preamble]
        if not canSum(sum_candidates, n):
            return n


def findWeakness(numbers, invalid):
    # get a contiguous range of numbers that adds to invalid
    for i, n in enumerate(numbers):
        s = 0
        # add the numbers after this one until we hit or are over target
        for j in range(i, len(numbers)):
            s += numbers[j]
            if s >= invalid:
                break

        if s == invalid:
            # return sum of smallest and largest in range
            cset = numbers[i : j + 1]
            cset.sort()
            return cset[0] + cset[-1]


with open("./day9/input.py") as f:
    numbers = [int(n) for n in f.read().strip().split("\n")]
    invalid = findInvalid(numbers, 25)
    print(f"Invalid number is {invalid}")
    print(findWeakness(numbers, invalid))
