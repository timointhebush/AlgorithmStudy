def solution(distance, rocks, n):
    rocks.sort()
    left, right = 1, distance
    ans = 0
    while left <= right:
        cnt = 0
        mid = (left + right)//2
        prev_rock = 0
        for rock_pos in rocks:
            if rock_pos - prev_rock < mid:
                cnt += 1
            else:
                prev_rock = rock_pos
        if distance - prev_rock < mid:
            cnt += 1
        if cnt > n:
            right = mid - 1
        else: #cnt <= n
            if mid > ans: #최소 거리의 최댓값을 구하는거니까..?
                ans = mid
            left = mid + 1
    return ans

print(solution(25, [2, 14, 11, 21, 17], 2))