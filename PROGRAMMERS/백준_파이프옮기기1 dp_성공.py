import sys


def solution():
    N = int(sys.stdin.readline().strip())
    home = [[0 for _ in range(N)] for _ in range(N)]
    for ri_tmp in range(N):
        tmp = sys.stdin.readline().strip().split(" ")
        for ci_tmp in range(N):
            home[ri_tmp][ci_tmp] = int(tmp[ci_tmp])
    # 0 : 가로, 1: 세로, 2: 대각선
    dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
    dp[0][0][1] = 1
    # 시작부터 가로로 움직이는 경우
    for c in range(2, N):
        if home[0][c] != 1:
            dp[0][0][c] = dp[0][0][c - 1]

    for row in range(1, N):
        for col in range(2, N):
            # 대각선
            if home[row][col] != 1 and home[row - 1][col] != 1 and home[row][col - 1] != 1:
                dp[2][row][col] = (
                    dp[0][row - 1][col - 1] + dp[1][row - 1][col - 1] + dp[2][row - 1][col - 1]
                )
            # 가로
            if home[row][col] != 1:
                dp[0][row][col] = dp[0][row][col - 1] + dp[2][row][col - 1]
                dp[1][row][col] = dp[1][row - 1][col] + dp[2][row - 1][col]
    return dp[0][N - 1][N - 1] + dp[1][N - 1][N - 1] + dp[2][N - 1][N - 1]


print(solution())
