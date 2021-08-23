from itertools import permutations

def solution(n, weak, dist):
    w_num = len(weak)
    cand = []
    # weak을 선형 구조로 생성
    new_weak = [ n+w for w in weak ]
    weak += new_weak
    friends_list = permutations(dist)
    # friends_list = [ (40,30,10,5,1) ]
    for friends in friends_list:
        for start_idx in range(w_num):
            pos = weak[start_idx]
            for f_num, friend in enumerate(friends):
                pos += friend
                if pos >= weak[ start_idx + w_num - 1 ]:
                    cand.append(f_num+1)
                    break
                else:
                    for w in weak:
                        if w > pos:
                            pos = w
                            break
    # print(cand)
    return -1 if len(cand) == 0 else min(cand)



# print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
# print(solution(30, [0, 3, 11, 21], [10, 4]))
print(solution(200, [0, 10, 50, 80, 120, 160], [1, 5, 10, 30, 40]))