from itertools import combinations

def solution(orders, course):
    answer = []
    cand = {}
    for c in course:
        cand[c] = {}
    for order in orders:
        for c in course:
            for comb in combinations(order, c):
                comb_str = "".join(sorted(comb))
                if comb_str not in cand[c]:
                    cand[c][comb_str] = 1
                else:
                    cand[c][comb_str] += 1
    for c in course:
        max_num = max( cand[c].values() )
        if max_num >= 2:
            for comb, num in cand[c].items():
                if num == max_num: answer.append(comb)
    return sorted(answer)

print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
# print(solution(["ABCD", "ABCD", "ABCD"], [2,3,4]))
# print(solution(['AB', 'CD','CD','CD','CD','CDE' ], [1, 2, 3]))