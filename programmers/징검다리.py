def solution(distance, rocks, n):
    answer = 0
    left, right = 1, distance
    rocks.sort()
    while left <= right:
        tmp_min_gap = (left + right) // 2
        pre_rock = 0
        tmp_n = 0
        is_over = False
        for rock in rocks:
            if rock - pre_rock < tmp_min_gap:
                tmp_n += 1
                if tmp_n > n:
                    is_over = True
                    break
            else:
                pre_rock = rock
        if is_over:
            right = tmp_min_gap - 1
        else:
            answer = max(answer, tmp_min_gap)
            left = tmp_min_gap + 1
    return answer


if __name__ == "__main__":
    print(solution(25, [2, 14, 11, 21, 17], 2))