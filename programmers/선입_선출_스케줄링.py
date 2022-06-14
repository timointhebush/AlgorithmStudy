def solution(n, cores):
    if n <= len(cores):
        return n
    n -= len(cores)
    left, right = 1, max(cores) * n
    while left < right:
        mid = (left + right) // 2
        num_job_done = 0
        for core in cores:
            num_job_done += mid // core
        if n <= num_job_done: # 일을 더많이 -> 시간을 줄여야 함.
            right = mid
        else: # n >= num_job_done : 일을 적게함 -> 시간을 늘려야함
            left = mid + 1
    time_job_done = right
    for core in cores:
        n -= (time_job_done - 1) // core
    for i, core in enumerate(cores):
        if time_job_done % core == 0:
            n -= 1
            if n == 0:
                return i + 1


print(solution(6, [1, 2, 3]))