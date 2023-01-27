import re


def group_sum_all(answers):
    ind_ans = [set(a) for a in answers.split("\n")]

    # if only one person in group, return num unique answers
    if len(ind_ans) == 1:
        return len(ind_ans[0])

    # if multiple people in group, check how many of first person's answers are in all other people's answers
    return len(ind_ans[0].intersection(*ind_ans[1:]))


def group_sum_any(answers):
    return len(set([a for a in list(answers) if re.match(r"[a-z]", a)]))


if __name__ == "__main__":
    with open("./day6/input.txt") as f:
        grouped_answers = f.read().split("\n\n")

    print(f"Any: {sum([group_sum_any(ans) for ans in grouped_answers])}")
    print(f"All: {sum([group_sum_all(ans) for ans in grouped_answers])}")