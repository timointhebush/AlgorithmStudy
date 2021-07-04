def solution(n, times):
    min_time = 1
    max_time = max(times) * n
    answer = max_time
    while min_time <= max_time:
        handled_num = 0
        mid_time = (min_time + max_time) // 2
        for time in times:
            handled_num += mid_time // time
        if handled_num < n:
            min_time = mid_time + 1
        else: #handled_num >= n
            if mid_time <= answer:
                answer = mid_time
            max_time = mid_time - 1
    return answer

#내가 처음 시도했던 이분탐색과 다른점, 내가 해던것은 정확한 한 지점을 찾고
#여기는 그걸 향해 다가가다가 최대한 근접하면 중지하는 느낌..

print(solution(1000000000, [1, 1000000000, 1000000000]))