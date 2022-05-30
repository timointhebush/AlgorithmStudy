def solution(citations):
    citations.sort()
    h = len(citations)
    while h > 0 and citations[len(citations)-h] < h:
        h -= 1
    return h

print(solution([0, 0, 0, 0] ))
