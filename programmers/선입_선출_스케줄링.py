def solution(n, cores):
    n_cores = len(cores)
    if n <= n_cores:
        return n_cores
    n -= n_cores
    left, right = 1, n * max(cores)
    # print('n', n)
    while left < right:
        # print("l", left, "r", right)
        mid = (left + right) // 2
        # print("mid", mid)
        n_job_done = 0
        for core in cores:
            n_job_done += mid // core
        # print('job', n_job_done)
        if n_job_done < n:
            left = mid + 1
        else:  # n_job_done > n
            right = mid
        # print()
    # print(mid)
    # print(n_job_done)
    for core in cores:
        n -= (right - 1) // core

    for i, core in enumerate(cores):
        # print('i', i)
        if right % core == 0:
            n -= 1
            if n == 0:
                return i + 1