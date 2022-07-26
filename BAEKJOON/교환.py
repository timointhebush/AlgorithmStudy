from itertools import combinations
from collections import deque
import copy


def bfs():
    global l
    visited = set()
    ans = 0
    len_q = len(q)
    # print(len_q)
    for _ in range(len_q):
        list_num = list(str(q.popleft()))
        for i, j in ij_cases:
            l += 1
            copy_list_num = copy.deepcopy(list_num)
            copy_list_num[i], copy_list_num[j] = copy_list_num[j], copy_list_num[i]
            if copy_list_num[0] == '0':
                continue
            copy_num = int("".join(copy_list_num))
            if copy_num not in visited:
                ans = max(ans, copy_num)
                visited.add(copy_num)
                q.append(copy_num)
    return ans


if __name__ == "__main__":
    l = 0

    N, K = map(int, input().split())
    q = deque([N])
    list_N = list(str(N))
    M = len(list_N)
    ij_cases = list(combinations(range(M), 2))
    # print(ij_cases)

    ans = 0
    for _ in range(K):
        ans = bfs()

    if not ans:
        print(-1)
    else:
        print(ans)
    print(l)

# def bfs():
#     visited = set()
#     ans = 0
#     qlen = len(q)
#     print(qlen)
#     while qlen:
#         num = q.popleft()
#         list_num = list(str(num))
#         for i, j in ij_cases:
#             copy_list_num = copy.deepcopy(list_num)
#             temp_i, temp_j = copy_list_num[i], copy_list_num[j]
#             copy_list_num[i], copy_list_num[j] = temp_j, temp_i
#             if copy_list_num[0] == '0':
#                 continue
#             copy_num = int(''.join(copy_list_num))
#             if copy_num not in visited:
#                 ans = max(ans, copy_num)
#                 visited.add(copy_num)
#                 q.append(copy_num)
#         qlen -= 1
#     return ans
#
# N, K = map(int, input().split())
# list_N = [i for i in range(len(str(N)))]
# ij_cases = list(combinations(list_N, 2))
# q = deque()
# q.append(N)
#
# ans = 0
# while K:
#     ans = bfs()
#     K -= 1
# if not ans:
#     print(-1)
# else:
#     print(ans)