def solution(n, t, m, timetable):
    answer = ''
    timetableM = []
    for time in timetable:
        if time != "23:59":
            tmp = time.split(":")
            timetableM.append(int(tmp[0])*60 + int(tmp[1]))
    timetableM = sorted(timetableM)
    if len(timetableM) == 0:
        return toTime(9*60 + (n-1)*t)
    
    busTable = []
    for num in range(n):
        busTable.append(9*60 + (num-1)*t)
    
    boarded = []
    for busT in busTable:
        for _ in range(m):
            if not timetableM:
                return toTime(9*60 + (n-1)*t)
            if timetableM[0] > busT:
                break
            boarded.append(timetableM[0])
            timetableM.pop(0)

    if timetableM:
        return toTime(timetableM[-1]-1)
    else:
        return toTime(brink - 1) 

def toTime(minute):
    hour = minute // 60
    return f"{hour:02d}:{minute%60:02d}"

print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))

print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))

print(solution(1, 1, 5, ["00:00", "00:00", "00:00", "00:00", "00:01", "00:02", "00:03", "00:04"]))