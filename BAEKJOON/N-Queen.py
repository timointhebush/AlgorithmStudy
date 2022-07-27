N = int(input())

answer = 0
board = [0] * N


def can_put(r):
    for prev_r in range(r):
        if (board[prev_r] == board[r]) or abs(prev_r - r) == abs(board[prev_r] - board[r]):
            return False
    return True


def dfs(r):
    global answer
    if r == N:
        answer += 1
        return
    else:
        for c in range(N):
            board[r] = c
            if can_put(r):
                dfs(r + 1)


dfs(0)
print(answer)