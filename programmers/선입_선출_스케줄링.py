def solution(n, cores):
    num_cores = len(cores)
    if n <= num_cores:
        return n

    n -= num_cores

    min_time, max_time = 1, max(cores) * n
    while min_time < max_time:
        tmp_time = (min_time + max_time) // 2
        num_task_done = 0
        for core_time in cores:
            num_task_done += tmp_time // core_time

        if num_task_done < n:
            min_time = tmp_time + 1
        else:
            max_time = tmp_time

    left_task = n
    for core_time in cores:
        left_task -= (max_time - 1) // core_time

    for i, core_time in enumerate(cores):
        if max_time % core_time == 0:
            left_task -= 1
            if left_task == 0:
                return i + 1


if __name__ == "__main__":
    print(solution(6, [1, 2, 3]))