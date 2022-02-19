def solution(money):
    results = []
    #첫번째 집이 털린경우 (마지막집 안털림)
    max_theft = [0 for i in range(len(money))]
    max_theft[0] = money[0]
    max_theft[1] = money[0]
    for i in range(2, len(money)-1):
        max_theft[i] = max(max_theft[i-1], max_theft[i-2] + money[i])
    results.append(max_theft[len(money)-2])

    #첫번째 집이 털리지 않은 경우, (마지막 집 털림)
    max_theft = [0 for i in range(len(money))]
    max_theft[1] = money[1]
    for i in range(2, len(money)):
        max_theft[i] = max(max_theft[i-1], max_theft[i-2] + money[i])
    results.append(max_theft[len(money)-1])
    return max(results)



print(solution([1, 1, 4, 1, 4]))