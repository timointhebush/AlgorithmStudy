def solution(lines):
    logs = []
    for line in lines:
        date, time, processing_sec = line.split()
        processing_milli_sec = float(processing_sec[:-1]) * 1000
        hour, minute, sec = map(float, time.split(":"))
        end_milli_sec = hour * 60 * 60 * 1000 + minute * 60 * 1000 + sec * 1000
        start_milli_sec = end_milli_sec - processing_milli_sec + 1
        logs.append([start_milli_sec, end_milli_sec])
    answer = 0
    for start_end in logs:
        for d in start_end:
            tmp_ans = 0
            for log in logs:
                if log[0] <= d <= log[1] or log[0] <= d + 1000 <= log[1]:
                    tmp_ans += 1
                answer = max(tmp_ans, answer)
    return answer


print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))