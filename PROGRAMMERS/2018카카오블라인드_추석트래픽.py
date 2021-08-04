def solution(lines):
    answer = 0
    if len(lines) == 1:
        return 1
    startList, endList = [], []
    for line in lines:
        end = line[11:23].split(":")
        end = int(end[0]) * 3600 + int(end[1]) * 60 + float(end[2])
        start = round(end - float(line[24:-1]) + 0.001, 3)
        startList.append(start)
        endList.append(end)
    for idx, end in enumerate(endList[:-1]):
        num = 0
        scope = round(end + 1.0 - 0.001, 3)
        for start in startList[idx:]:
            if scope < start:
                pass
            else:
                num += 1
        answer = max(answer, num)
    return answer

print(solution([
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]))

print(solution([
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]))

print(solution( [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
] ))

print(solution(["2016-09-15 00:00:00.000 3s"]))

print(solution(["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"]))