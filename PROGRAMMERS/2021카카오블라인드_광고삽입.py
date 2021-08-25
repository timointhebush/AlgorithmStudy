def solution(play_time, adv_time, logs):
    play_sec, adv_sec = toSeconds(play_time), toSeconds(adv_time)
    new_logs = []
    for log in logs:
        tmp = log.split("-")
        start, end = toSeconds(tmp[0]), toSeconds(tmp[1])
        new_logs.append( (start, end) )
    new_logs = sorted(new_logs, key=lambda x : x[0])
    cand = {}
    # print(new_logs)
    for i, log in enumerate(new_logs):
        adv_start_sec = log[0]
        adv_end_sec = adv_start_sec + adv_sec
        accumWatch = 0
        if adv_end_sec <= play_sec:
            for start_sec, end_sec in new_logs[i:]:
                accumWatch += getWatchSec((start_sec, end_sec), (adv_start_sec, adv_end_sec))
        cand[ toTime(adv_start_sec) ] = accumWatch
    max_watch_sec = max(cand.values())
    if max_watch_sec == 0:
        return toTime(0)
    cand_max_start_sec = []
    for key, val in cand.items():
        if val == max_watch_sec:
            cand_max_start_sec.append(key)
    return min(cand_max_start_sec)

def toSeconds(time):
    tmp = time.split(":")
    return int(tmp[0])*3600 + int(tmp[1])*60 + int(tmp[2])

def toTime(seconds):
    hours = seconds//3600
    minutes = (seconds%3600) // 60
    seconds = (seconds%3600) % 60
    return f"{hours:02d}"+":"+f"{minutes:02d}"+":"+f"{seconds:02d}"

def getWatchSec(log, adv):
    if adv[1] <= log[0] or adv[0] >= log[1]:
        return 0
    if adv[0] <= log[0] <= adv[1] and adv[1] <= log[1]:
        return adv[1] - log[0]
    if adv[0] <= log[1] <= adv[1] and adv[0] >= log[0]:
        return log[1] - adv[0]
    if adv[0] >= log[0] and adv[1] <= log[1]:
        return adv[1] - adv[0]
    else:
        return log[1] - log[0]


print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))

print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))