def solution(lines):
    num_log = len(lines)
    start_end_milli_sec = []
    for log in lines:
        _, end_time, process_milli_sec = log.split(" ")
        hour, minute, sec = map(float, end_time.split(":"))
        end_milli_sec = int(hour) * 60 * 60 * 1000 + int(minute) * 60 * 1000 + int(sec * 1000)
        start_milli_sec = end_milli_sec - int(float(process_milli_sec[:-1]) * 1000) + 1
        start_end_milli_sec.append([start_milli_sec, end_milli_sec])

    answer = 1
    for i in range(num_log - 1):
        tmp_answer = 1
        ref_start = start_end_milli_sec[i][1]
        ref_end = ref_start + 999
        for j in range(i + 1, num_log):
            log_start, log_end = start_end_milli_sec[j]
            if log_end >= ref_start and log_start <= ref_end:
                tmp_answer += 1
        answer = max(answer, tmp_answer)
    return answer


if __name__ == "__main__":
    print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))
    # print(solution([
    #     "2016-09-15 20:59:57.421 0.351s",
    #     "2016-09-15 20:59:58.233 1.181s",
    #     "2016-09-15 20:59:58.299 0.8s",
    #     "2016-09-15 20:59:58.688 1.041s",
    #     "2016-09-15 20:59:59.591 1.412s",
    #     "2016-09-15 21:00:00.464 1.466s",
    #     "2016-09-15 21:00:00.741 1.581s",
    #     "2016-09-15 21:00:00.748 2.31s",
    #     "2016-09-15 21:00:00.966 0.381s",
    #     "2016-09-15 21:00:02.066 2.62s"
    # ]))
