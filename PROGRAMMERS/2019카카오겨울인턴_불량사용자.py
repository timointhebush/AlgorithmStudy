from itertools import permutations


def solution(user_id, banned_id):
    answer = 0
    cand = {}
    for case in permutations(user_id, len(banned_id)):
        if check(case, banned_id):
            case = tuple(sorted(case))
            if case not in cand:
                cand[case] = True
    return len(cand)


def check(case, banned_id):
    for i in range(len(case)):
        if len(case[i]) != len(banned_id[i]):
            return False
        for j in range(len(case[i])):
            if banned_id[i][j] != "*" and case[i][j] != banned_id[i][j]:
                return False
    return True


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(
    solution(
        ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]
    )
)
