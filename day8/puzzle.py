def parseInstruction(inst):
    return inst[:3], int(inst[6:]) * (1 if inst[4] == "+" else -1)


def getValue(instructions, preLoop=False):
    accumulator = 0
    inst_idx = 0
    visited = [False] * len(instructions)

    while True:
        if inst_idx >= len(instructions):
            return accumulator

        if visited[inst_idx]:
            return accumulator if preLoop else None

        visited[inst_idx] = True
        op, arg = parseInstruction(instructions[inst_idx])

        if op == "nop":
            inst_idx += 1
        elif op == "acc":
            accumulator += arg
            inst_idx += 1
        else:
            inst_idx += arg


def fix(instructions):
    for i, inst in enumerate(instructions):
        if inst[:3] == "acc":
            continue
        elif inst[:3] == "nop":
            instructions[i] = inst.replace("nop", "jmp")
        elif inst[:3] == "jmp":
            instructions[i] = inst.replace("jmp", "nop")

        if terminateVal := getValue(instructions):
            return terminateVal

        instructions[i] = inst


if __name__ == "__main__":
    with open("./day8/input.py") as f:
        instructions = f.read().strip().split("\n")

    print(
        f"The value right before the program loops is {getValue(instructions, preLoop=True)}"
    )

    print(
        f"With one change, the value after the program terminates is {fix(instructions)}"
    )

