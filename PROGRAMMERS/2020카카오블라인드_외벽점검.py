def solution(n, weak, dist):
    answer = 0
    d = len(dist)
    for i in range(-1, -d-1, -1):
        if tryCheck(n, weak, dist[i:]) == True:
            return -1 * i
    return -1

def tryCheck(n, weak, dsitPart):
    for w in weak:
        checked = {}
        for d in dsitPart[::-1]:
            clockP = w + d
            checkBetween(n, weak, start, clockP)
            counterClockP = w - d

def checkBetween(n, weak, start, point):
    if point 

print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))