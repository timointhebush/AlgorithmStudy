def solution(answers):
    answer = []
    _1 = [1, 2, 3, 4, 5]
    _2 = [2, 1, 2, 3, 2, 4, 2, 5]
    _3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score1 = 0
    score2 = 0
    score3 = 0
    for idx in range(len(answers)):
        if answers[idx] == _1[idx % 5]:
            score1 += 1
        if answers[idx] == _2[idx % 8]:
            score2 += 1
        if answers[idx] == _3[idx % 10]:
            score3 += 1
    tmp = [score1, score2, score3]
    highest = max(tmp)
    for student in range(3):
        if highest == tmp[student]:
            answer.append(student+1)
    return answer

print(solution([1,3,2,4,2]))