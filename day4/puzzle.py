import re
import functools


def validateYr(yr, minYr, maxYr):
    return int(yr) >= minYr and int(yr) <= maxYr


def validateHgt(hgt):
    if hgt[-2:] == "cm":
        num = int(hgt[:-2])
        return num >= 150 and num <= 193
    elif hgt[-2:] == "in":
        num = int(hgt[:-2])
        return num >= 59 and num <= 76

    # Invalid format
    return False


def validateHcl(hcl):
    return re.match(r"#[0-9a-f]{6}$", hcl) is not None


def validateEcl(ecl):
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def validatePid(pid):
    return len(pid) == 9 and pid.isdigit()


validators = {
    "byr": functools.partial(validateYr, minYr=1920, maxYr=2002),
    "iyr": functools.partial(validateYr, minYr=2010, maxYr=2020),
    "eyr": functools.partial(validateYr, minYr=2020, maxYr=2030),
    "hgt": validateHgt,
    "hcl": validateHcl,
    "ecl": validateEcl,
    "pid": validatePid,
    "cid": lambda c: True,
}

mandatory_keys = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
]


def isValid(passport):
    # Expects a string representation of a passport
    fields = re.split(r"[ \n]", passport)
    fields = [(f.split(":")[0], f.split(":")[1]) for f in fields]

    # Are all mandatory keys there?
    if not all(k in [f[0] for f in fields] for k in mandatory_keys):
        return False

    # Are all fields valid?
    for field in fields:
        if not validators[field[0]](field[1]):
            return False

    return True


if __name__ == "__main__":
    with open("./day4/input.txt") as f:
        contents = f.read()
        passports = contents.split("\n\n")
        print(sum(map(lambda p: isValid(p), passports)))