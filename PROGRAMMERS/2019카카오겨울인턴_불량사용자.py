def solution(user_id, banned_id):
    used = {_: False for _ in user_id}
    cand = {_: [] for _ in banned_id}
    no_overlap_banned = list(set(banned_id))
    for banned in no_overlap_banned:
        for user in user_id:
            if check(user, banned):
                cand[banned].append(user)
    global answer_set, board, answer
    answer = 0
    board = []
    for banned in banned_id:
        board.append(cand[banned])
    print(board)
    answer_set = set()
    dfs(0)
    return answer


def check(user, banned):
    n_user, n_banned = len(user), len(banned)
    if n_user != n_banned:
        return False
    for i in range(n_banned):
        if banned[i] != "*" and user[i] != banned[i]:
            return False
    return True


def dfs(row):
    global answer_set
    if row == len(board):
        if len(answer_set) == len(board):
            



print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(
    solution(
        ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]
    )
)
