def solution(user_id, banned_id):
    answer = 1
    cand = {}
    no_overlap_banned = list(set(banned_id))
    for banned in no_overlap_banned:
        cnt = 0
        for user in user_id:
            if check(user, banned):
                cnt += 1
        cand[banned] = cnt
    print(cand)
    for banned in banned_id:
        answer *= cand[banned]
        cand[banned] -= 1
    return answer


def check(user, banned):
    n_user, n_banned = len(user), len(banned)
    if n_user != n_banned:
        return False
    for i in range(n_banned):
        if banned[i] != "*" and user[i] != banned[i]:
            return False
    return True


# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(
    solution(
        ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]
    )
)
