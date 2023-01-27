import functools


def find_earliest_bus(et, ids):
    # minutes to wait from earliest timestamp to the next bus for each bus id
    mtw = [i - (et % i) for i in ids]
    # earliest bus id
    eb = ids[mtw.index(min(mtw))]

    print(f"The earliest bus is {eb}, waiting for {min(mtw)} minutes: {min(mtw) * eb}")


def find_earliest_timestamp(ids):
    # TODO this solution works but is WAY too slow for the puzzle input

    # find the earliest timestamp such that the first bus ID departs at that time
    # and each subsequent listed bus ID departs at that subsequent minute.
    buses = [i for i in ids if i != "x"]

    # our first bus is mod 0, start at timestamp 0
    step = buses[0]
    ts = 0

    # doesn't matter what order we do rest, should be more efficient sorted
    buses = buses[1:]
    buses.sort()
    for bus in buses:
        while bus - (ts % bus) != ids.index(bus):
            ts += step

        # we've found a ts for which all buses to this point have the correct mtw
        step = step * bus  # little bit of a cheat, all our buses are prime
        print(f"after bus {bus}, step is {step}")

    print(ts)


with open("./day13/input.txt") as f:
    notes = f.read().strip().split("\n")

    # part 1
    find_earliest_bus(
        int(notes[0]), [int(bus) for bus in notes[1].split(",") if bus != "x"]
    )

    # part 2
    find_earliest_timestamp(
        [int(bus) if bus != "x" else bus for bus in notes[1].split(",")]
    )

