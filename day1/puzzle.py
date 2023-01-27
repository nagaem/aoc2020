from pathlib import Path

def fixExpenseReportTwoNumbers(report):
    # sort report
    report.sort()

    # add expenses from beginning of report and end of report together 
    # (smallest and largest) until either < 2020 (we know exp1 can't be)
    # the one) or == 2020 (we have our answer)
    for exp1 in report:
        exp2_idx = len(report) - 1
        while (total := exp1 + report[exp2_idx]) > 2020:
            exp2_idx -= 1
        
        if total == 2020:
            return exp1 * report[exp2_idx]


def fixExpenseReportThreeNumbers(report):
    # sort report
    report.sort()

    # similar strategy to last time, with adjustment for second number
    for idx1 in range(len(report) - 2):
        idx2 = idx1 + 1
        idx3 = len(report) - 1

        # if they're all over 2020, last one is too big
        while (report[idx1] + report[idx2] + report[idx3]) > 2020:
            idx3 -= 1
        
        # if we're under 2020 now, try increasing the second one
        while (total := report[idx1] + report[idx2] + report[idx3]) < 2020:
            idx2 += 1
            if idx2 == idx3:
                break
        
        # if we hit the goal, return; else try again from the next idx1
        if total == 2020:
            print(f"Values are {report[idx1]} {report[idx2]} {report[idx3]}")
            return report[idx1] * report[idx2] * report[idx3]


def main():
    # read expense report
    report = []
    with open(Path("day1/input.txt")) as file:
        for line in file:
            report.append(int(line.strip()))
    
    # report = [1721, 979, 366, 299, 675, 1456]
    print(fixExpenseReportThreeNumbers(report))

if __name__ == "__main__":
    main()
