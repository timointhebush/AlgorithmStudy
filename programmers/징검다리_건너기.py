def solution(stones, k):
    answer = 0
    while is_crossable(stones, k):
        min_num = min_not_zero(stones)
        stones = list(map(lambda x: x - min_num, stones))
        answer += min_num
    return answer


def is_crossable(stones, k):
    max_n_empty = 0
    j = -1
    for i in range(len(stones)):
        if i > j and stones[i] <= 0:
            n_empty = 1
            j = i + 1
            while j < len(stones) and stones[j] <= 0:
                n_empty += 1
                j += 1
            if n_empty > max_n_empty:
                max_n_empty = n_empty
    return max_n_empty < k


def min_not_zero(stones):
    min_num = float('inf')
    for stone in stones:
        if 0 < stone < min_num:
            min_num = stone
    return min_num


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
# print(is_crossable([0, 1, 2, 0, 0, 0, 1, 0, 2, 0], 3))
# print(is_crossable([0], 0))