from math import radians, sin, cos, atan2, hypot, degrees

directions = {"E": (1, 0), "N": (0, 1), "W": (-1, 0), "S": (0, -1)}


def get_manhattan_distance_2(inst):
    ship_loc = [0, 0]
    waypoint_loc = [10, 1]  # relative to ship

    for i in inst:
        action = i[0]
        val = i[1]

        if action in directions:
            waypoint_loc[0] += val * directions[action][0]
            waypoint_loc[1] += val * directions[action][1]
        elif action == "F":
            ship_loc[0] += val * waypoint_loc[0]
            ship_loc[1] += val * waypoint_loc[1]
        elif action in ["L", "R"]:
            waypoint_angle = degrees(atan2(waypoint_loc[1], waypoint_loc[0]))
            waypoint_dist = hypot(waypoint_loc[0], waypoint_loc[1])

            if action == "L":
                waypoint_angle += val
            else:
                waypoint_angle -= val

            waypoint_loc = [
                waypoint_dist * cos(radians(waypoint_angle)),
                waypoint_dist * sin(radians(waypoint_angle)),
            ]

        # print(
        #     f"After instruction {i}, ship is at {ship_loc} and waypoint is at {waypoint_loc}"
        # )

    return int(abs(ship_loc[0]) + abs(ship_loc[1]))


def get_manhattan_distance_1(inst):
    location = [0, 0]
    angle = 0

    for i in inst:
        action = i[0]
        val = i[1]
        if action in directions:
            location[0] += val * directions[action][0]
            location[1] += val * directions[action][1]
        elif action == "L":
            angle += val % 360
            angle % 360
        elif action == "R":
            angle -= val % 360
            if angle < 0:
                angle = 360 + angle
        elif action == "F":
            angle_rad = radians(angle)
            location[0] += val * int(cos(angle_rad))
            location[1] += val * int(sin(angle_rad))

    # Done instructions, calculate distance
    return abs(location[0]) + abs(location[1])


with open("./day12/input.txt") as f:
    instructions = [(row[0], int(row[1:])) for row in f.read().strip().split("\n")]

print(f"Part 1: {get_manhattan_distance_1(instructions)}")
print(f"Part 2: {get_manhattan_distance_2(instructions)}")
