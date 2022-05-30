from collections import deque

def solution(n, t, m, timetable):
    timetable = deque(sorted(map(toMinute, timetable)))
    for N in range(n):
        bus = []
        M = 0
        currentBus = 540 + t*N
        while timetable and M < m and timetable[0] <= currentBus:
            bus.append(timetable.popleft()) 
            M += 1
        if N == n-1: # 마지막
            if len(bus) < m:
                return(toTime(currentBus))
            else:
                return(toTime(bus[-1] - 1))

def toTime(minute):
    hour = minute // 60
    return f"{hour:02d}:{minute%60:02d}"

def toMinute(time):
    tmp = time.split(":")
    return int(tmp[0])*60 + int(tmp[1])

print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))

print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))

print(solution(1, 1, 5, ["00:00", "00:00", "00:00", "00:00", "00:01", "00:02", "00:03", "00:04"]))