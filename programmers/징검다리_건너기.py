def solution(stones, k):
    left, right = 1, 200000000
    while left < right:
        mid = (left + right) // 2
        empty_cnt = 0
        for stone in stones:
            if (stone - mid) <= 0:
                empty_cnt += 1
            else:
                empty_cnt = 0
        if k <= empty_cnt: # 줄임.
            right = mid - 1
        else:
            left = mid + 1
    return left - 1


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))