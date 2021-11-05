import sys


def solution():
    global N, ans
    N = int(sys.stdin.readline().strip())
    home = [[1 for _ in range(N + 2)] for _ in range(N + 2)]
    for ri_tmp in range(N):
        tmp = sys.stdin.readline().strip().split(" ")
        for ci_tmp in range(N):
            home[ri_tmp + 1][ci_tmp + 1] = int(tmp[ci_tmp])
    pipe = ((1, 1), (1, 2))
    ans = 0
    dfs(pipe, home)
    return ans


def dfs(pipe, home):
    global ans
    if pipe[1] == (N, N):
        ans += 1
        return 0
    next_cases = get_next_cases(pipe, home)
    if len(next_cases) >= 1:
        for next_pipe in next_cases:
            dfs(next_pipe, home)


def get_next_cases(pipe, home):
    A, B = pipe
    if pipe[0][0] == pipe[1][0]:  # 가로
        cand = [((A[0], A[1] + 1), (B[0], B[1] + 1)), ((A[0], A[1] + 1), (B[0] + 1, B[1] + 1))]
    elif pipe[0][1] == pipe[1][1]:  # 세로
        cand = [((A[0] + 1, A[1]), (B[0] + 1, B[1])), ((A[0] + 1, A[1]), (B[0] + 1, B[1] + 1))]
    else:  # 대각선
        cand = [
            ((A[0] + 1, A[1] + 1), (B[0], B[1] + 1)),
            ((A[0] + 1, A[1] + 1), (B[0] + 1, B[1])),
            ((A[0] + 1, A[1] + 1), (B[0] + 1, B[1] + 1)),
        ]
    cleanse_cases(cand, home)
    return cand


def cleanse_cases(cand, home):
    del_idx_list = []
    for i, pipe in enumerate(cand):
        A, B = pipe
        if pipe[0][0] == pipe[1][0] or pipe[0][1] == pipe[1][1]:  # 가로, 세로
            if home[B[0]][B[1]] == 1:
                del_idx_list.append(i)
        else:  # 대각선
            if home[B[0]][B[1]] == 1 or home[B[0] - 1][B[1]] == 1 or home[B[0]][B[1] - 1] == 1:
                del_idx_list.append(i)
    for i in del_idx_list[::-1]:
        del cand[i]


print(solution())
