def solution(stones, k):
    answer = 1
    left, right = 1, 2 * (10 ** 8)
    while left <= right:
        mid = (left + right) // 2
        if is_crossable(stones, k, mid):
            left = mid + 1
            answer = max(answer, mid)
        else:
            right = mid - 1
    return answer


def is_crossable(stones, k, mid):
    broken_stone = 0
    for stone in stones:
        if stone - mid < 0:
            broken_stone += 1
        else:
            broken_stone = 0
        if broken_stone == k:
            return False
    return True


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))