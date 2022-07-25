import sys


def dfs(r, c):
    if not is_in(r, c) or board[r][c] == 'H':
        return 0

    if visited[r][c]:
        print(-1)
        exit()

    cache = dp[r][c]
    if cache != -1:
        return cache

    visited[r][c] = 1

    cache = 0
    for dir in range(4):
        nr = r + dr[dir] * int(board[r][c])
        nc = c + dc[dir] * int(board[r][c])

        cache = max(cache, dfs(nr, nc) + 1)
    dp[r][c] = cache

    visited[r][c] = 0
    return cache


def is_in(r, c):
    return 0 <= r < N and 0 <= c < M


if __name__ == "__main__":
    sys.stdin = open("게임.txt", "r")
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    N, M = map(int, input().split())

    visited = [[0 for _ in range(M)] for _ in range(N)]
    dp = [[-1 for _ in range(M)] for _ in range(N)]
    board = []
    for n in range(N):
        row = list(input())
        board.append(row)

    print(dfs(0, 0))