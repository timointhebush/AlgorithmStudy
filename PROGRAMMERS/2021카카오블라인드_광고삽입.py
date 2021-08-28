from collections import deque

def solution(play_time, adv_time, logs):
    play_sec, adv_sec = toSeconds(play_time), toSeconds(adv_time)
    logs_sec = []
    for log in logs:
        tmp = log.split("-")
        start, end = toSeconds(tmp[0]), toSeconds(tmp[1])
        logs_sec.append( (start, end) )
    play = [0 for _ in range(play_sec+1)]
    
    for log in logs_sec:
        play[log[0]] += 1
        play[log[1]] -= 1

    for _ in range(2):
        for sec in range(1, play_sec+1):
            play[sec] += play[sec-1]

    max_start_adv_sec = 0
    max_sec = play[adv_sec-1] - play[0]
    
    for sec in range(play_sec - adv_sec + 1):
        accum_sec = play[sec + adv_sec] - play[sec]
        if accum_sec > max_sec:
            max_sec = accum_sec
            max_start_adv_sec = sec + 1
        
    return toTime(max_start_adv_sec)
        
def toSeconds(time):
    tmp = time.split(":")
    return int(tmp[0])*3600 + int(tmp[1])*60 + int(tmp[2])

def toTime(seconds):
    hours = seconds//3600
    minutes = (seconds%3600) // 60
    seconds = (seconds%3600) % 60
    return f"{hours:02d}"+":"+f"{minutes:02d}"+":"+f"{seconds:02d}"



print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))