import functools


def getArrangements(adapters):
    adapters.sort()
    arrToI = [0] * len(adapters)

    # one way to get to the first adapter
    arrToI[0] = 1

    # if jump from start to second <=3, we can take out the first one
    if adapters[1] <= 3:
        arrToI[1] = 2
    else:
        arrToI[1] = 1

    # if jump from start to third <= 3, we can take out either or both of the previous two
    if adapters[2] <= 3:
        arrToI[2] = 4
    # if jump from first to third <= 3, we can take out the second one
    elif adapters[2] - adapters[0] <= 3:
        arrToI[2] = 2
    # if neither of these is true, we can't take out any
    else:
        arrToI[2] = arrToI[1]

    # Apply this logic for the rest of the adapters
    for ind, adapter in enumerate(adapters[3:]):
        i = ind + 3
        # 3-jolt differences don't have the potential for rearrangement
        if adapter - adapters[i - 1] == 3:
            arrToI[i] = arrToI[i - 1]

        elif adapter - adapters[i - 2] == 3:
            # we can omit one middle adapter only
            arrToI[i] = arrToI[i - 1] * 2

        elif adapter - adapters[i - 3] <= 3:
            # eg 0-1-2-3
            # we can omit either or both middle adapters
            arrToI[i] = arrToI[i - 1] + arrToI[i - 2] + arrToI[i - 3]

        else:
            # gap to i-3 > 3
            if adapter - adapters[i - 2] < 3:
                # eg 0-3-4-5, we can omit one
                arrToI[i] = arrToI[i - 1] * 2

            else:
                # eg 0-1-4-5, 0-2-4-6 we can't omit any
                arrToI[i] = arrToI[i - 1]

    print(arrToI)
    return arrToI[-1]


def getOnesAndThrees(adapters):
    adapters.sort()

    # Get first diff
    ones = 1 if adapters[0] == 1 else 0
    # built-in device has a diff of three
    threes = 2 if adapters[0] == 3 else 1
    for i, adapter in enumerate(adapters):
        if i + 1 >= len(adapters):
            break

        if adapters[i + 1] - adapter == 1:
            ones += 1
        elif adapters[i + 1] - adapter == 3:
            threes += 1

    return ones, threes


with open("./day10/input.py") as f:
    adapters = [int(a) for a in f.read().strip().split("\n")]
    ones, threes = getOnesAndThrees(adapters)

    print(f"Found {ones} one-jolt and {threes} three-jolt differences.")
    print(ones * threes)

    print(getArrangements(adapters))
