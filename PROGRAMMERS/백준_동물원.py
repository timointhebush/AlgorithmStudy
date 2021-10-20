def solution():
    N = int(input())
    case0, case1, case2 = 1, 1, 1
    for _ in range(N - 1):
        n_case0 = case1 + case2
        n_case1 = case0 + case2
        n_case2 = case0 + case1 + case2
        case0, case1, case2 = n_case0, n_case1, n_case2
    return (case0 + case1 + case2) % 9901


print(solution())
