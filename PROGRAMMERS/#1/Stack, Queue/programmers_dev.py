def solution(progresses, speeds):
    answer = []
    while progresses:
        count = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        if count >= 1:
            answer.append(count)
        for idx, speed in enumerate(speeds):
            progresses[idx] += speed
    return answer

print(solution([93, 30, 55], [1, 30, 5]))