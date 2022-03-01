def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    left, right = 0, distance
    answer = 0
    while left <= right:
        removed_rocks = 0
        mid = (left + right) // 2
        left_rock = 0
        for right_rock in rocks:
            if (right_rock - left_rock) < mid:
                removed_rocks += 1
            else:
                left_rock = right_rock
        if removed_rocks > n:
            right = mid - 1
        else:
            if mid > answer:
                answer = mid
            left = mid + 1
    return answer


print(solution(25, [2, 14, 11, 21, 17], 2))
