def solution(n, times):
    min_time = binarySearch(0, max(times) * n, n, times)
    while True:
        handled_num = 0
        for time in times:
            handled_num += (min_time-1) // time
        if handled_num == n:
            min_time -= 1
        else:
            break
    return min_time

def binarySearch(min_time, max_time, target, times):
    goal = max_time
    mid_time = (min_time + max_time) / 2
    handled_num = 0
    for time in times:
        handled_num += mid_time // time
    if handled_num > target:
        return binarySearch(min_time, mid_time-1, target, times)
    elif handled_num < target:
        return binarySearch(mid_time+1, max_time, target, times)
    else: #handled_num == n
        return mid_time

#너무 바이너리 서치 고정적인 알고리즘이었나.. 빈틈이 있었다..

print(solution(2, [1, 2]))