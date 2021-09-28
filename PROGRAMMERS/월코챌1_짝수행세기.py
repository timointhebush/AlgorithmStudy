from itertools import combinations


def solution(a):
    answer = -1
    dfs(a, len(a[0]))
    return answer


def get_col_sum(a):
    n_row, n_col = len(a), len(a[0])
    col_sum = []
    for i in range(n_col):
        num = 0
        for j in range(n_row):
            num += a[j][i]
        col_sum.append(num)
    return col_sum


def dfs(a, n_col):
    num_one = 2
    row_cand = []
    while num_one <= n_col:
        for comb in combinations(range(n_col), num_one):
            mold = [0 for _ in range(n_col)]
            for i in range(num_one):
                mold[comb[i]] = 1
            row_cand.append(mold)
        num_one *= 2
    print(row_cand)


print(solution([[0, 1, 0], [1, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(solution([[1, 0, 0], [1, 0, 0]]))
print(solution([[1, 0, 0, 1, 1], [0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 1]]))
