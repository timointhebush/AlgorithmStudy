from itertools import combinations_with_replacement


def solution(n, info):
    best_differ = 0
    best_case_list = []

    for idx_cnt_case in combinations_with_replacement(range(11), n):
        tmp_ryan = [0 for _ in range(11)]
        for idx in idx_cnt_case:
            tmp_ryan[idx] += 1

        apeach_score, ryan_score = 0, 0
        for i in range(11):
            if info[i] != 0 or tmp_ryan[i] != 0:
                if info[i] < tmp_ryan[i]:
                    ryan_score += (10 - i)
                else:
                    apeach_score += (10 - i)

        if apeach_score < ryan_score:
            differ = ryan_score - apeach_score
            if differ == best_differ:
                best_case_list.append(tmp_ryan)
            elif differ > best_differ:
                best_differ = differ
                best_case_list = [tmp_ryan]

    if best_differ == 0:
        return [-1]
    else:
        best_case_list = sorted(best_case_list, key=lambda x: tuple([-x[i] for i in range(10, -1, -1)]))
        return best_case_list[0]


if __name__ == "__main__":
    print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
