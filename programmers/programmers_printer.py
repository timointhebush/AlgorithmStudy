def solution(priorities, location):
    answer = 0
    req = []
    for idx, priority in enumerate(priorities):
        req.append((priority, idx))
    while True:
        doc = req[0]
        if max(req)[0] <= doc[0]:
            if location == doc[1]:
                return answer + 1
            answer += 1
            req.pop(0)
        else:
            req.append(req.pop(0))

print(solution([1, 1, 9, 1, 1, 1], 0))