import sys


def solution():
    N, K = tuple(map(int, sys.stdin.readline().split(" ")))
    items = []
    for _ in range(N):
        items.append(tuple(map(int, sys.stdin.readline().split(" "))))
    dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
    for n in range(1, N + 1):
        w, v = items[n - 1]
        for k in range(1, K + 1):
            if w > k:
                dp[n][k] = dp[n - 1][k]
            else:
                dp[n][k] = max(dp[n - 1][k - w] + v, dp[n - 1][k])
    return dp[N][K]


print(solution())
