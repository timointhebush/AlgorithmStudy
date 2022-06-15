def solution(stones, k):
    left, right = 1, 200000
    while left < right:
        mid = (left + right) // 2
        max_empty = 0
        j = -1
        for i in range(len(stones)):
            if i > j and (stones[i] - mid) <= 0:
                n_empty = 1
                j = i + 1
                while j < len(stones) and (stones[j] - mid) <= 0:
                    n_empty += 1
                    j += 1
                max_empty = max(max_empty, n_empty)

        if max_empty <= k:
            left = mid
        else: # max_empty > k:
            right = mid - 1
    return left


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))