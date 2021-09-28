def solution(a):
    answer = 0
    n = len(a)
    left_min, right_min = float("inf"), float("inf")
    for i in range(n):
        target = a[i]
        num = 0
        left = a[:i]
        if len(left) != 0 and min(left) < target:
            num += 1
        right = a[i + 1 :]
        if len(right) != 0 and min(right) < target:
            num += 1
        if num <= 1:
            answer += 1
    return answer


print(solution([9, -1, -5]))
print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))
