def solution(play_time, adv_time, logs):
    play_sec = toSeconds(play_time)
    new_logs = [(0,0)]
    for log in logs:
        tmp = log.split("-")
        start, end = toSeconds(tmp[0]), toSeconds(tmp[1])
        new_logs.append( (start, end) )
    new_logs = sorted(new_logs, key=lambda x : x[0])
    adv_sec = toSeconds(adv_time)
    cand = {}
    # print(new_logs)
    for i in range(len(new_logs)):
        for end_i in [0,1]:
            adv_start = new_logs[i][end_i]
            adv_end = adv_start + adv_sec
            accumWatch = getAccumWatchSec(new_logs, range(len(new_logs)), (adv_start, adv_end))
            cand[toTime(adv_start)] = accumWatch
            # if adv_end <= play_sec:
            #     idx = i
            #     overlapped = []
            #     while idx < len(new_logs) and adv_end > new_logs[idx][0] :
            #         overlapped.append(idx)
            #         idx += 1
            #     print(toTime(adv_start), overlapped)
            #     accumWatch = getAccumWatchSec(new_logs, overlapped, (adv_start, adv_end))
            #     cand[toTime(adv_start)] = accumWatch
    # print(cand)
    max_watch_sec = max(cand.values())
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

def getAccumWatchSec(new_logs, overlapped, adv):
    sec = 0
    for idx in overlapped:
        # print(getWatchSec(new_logs[idx], adv))
        sec += getWatchSec(new_logs[idx], adv)
    return sec

print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))

print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))