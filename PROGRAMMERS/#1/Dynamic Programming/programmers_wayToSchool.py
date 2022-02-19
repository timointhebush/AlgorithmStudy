def solution(m, n, puddles):
    map = [[0 for j in range(m+1)] for i in range(n+1)]
    map[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if [i, j] in puddles:
                pass
            else:
                map[i][j] += map[i-1][j] + map[i][j-1]
    return map[n][m] % 1000000007

print(solution(4, 3, [[2, 2]]))