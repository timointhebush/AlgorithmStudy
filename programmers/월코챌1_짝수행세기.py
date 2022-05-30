from itertools import combinations


def solution(a):
    global answer, a_col_sum, row_cand
    answer = 0
    row_cand = create_row_cand(len(a[0]))
    a_col_sum = get_col_sum(a)
    dfs(a, [], len(a[0]))
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


def check_col(_a):
    _a_col_sum = get_col_sum(_a)
    for i, num in enumerate(_a_col_sum):
        if num > a_col_sum[i]:
            return False
    return True


def create_row_cand(n_col):
    num_one = 2
    row_cand = [[0 for _ in range(n_col)]]
    while num_one <= n_col:
        for comb in combinations(range(n_col), num_one):
            mold = [0 for _ in range(n_col)]
            for i in range(num_one):
                mold[comb[i]] = 1
            row_cand.append(mold)
        num_one *= 2
    return row_cand


def dfs(a, _a, n_col):
    global answer
    if len(_a) == len(a):
        if get_col_sum(a) == get_col_sum(_a):
            answer += 1
        return 0
    for row in row_cand:
        _a.append(row)
        if check_col(_a):
            dfs(a, _a, n_col)
        _a.pop()


# print(solution([[0, 1, 0], [1, 1, 1], [1, 1, 0], [0, 1, 1]]))
# print(solution([[1, 0, 0], [1, 0, 0]]))
print(solution([[1, 0, 0, 1, 1], [0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 1]]))
