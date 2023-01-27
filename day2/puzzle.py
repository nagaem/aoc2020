import re

def isValid1(line):
    minTimes, maxTimes, letter, password = re.split(r'[-: ]+', line)
    return (password.count(letter) >= int(minTimes) and password.count(letter) <= int(maxTimes))


def isValid2(line):
    pos1, pos2, letter, password = re.split(r'[-: ]+', line)
    # positions are 1-indexed, fix that, and XOR 
    return (password[int(pos1)-1] == letter) ^ (password[int(pos2)-1] == letter)

# todo could make a list comp / sum op
if __name__ == "__main__":
    count = 0
    with open("./day2/input.txt") as file:
        # taking advantage of the bool/int relationship in python
        # print(sum(map(lambda l: isValid1(l.strip()), file)))
        print(sum(map(lambda l: isValid2(l.strip()), file)))