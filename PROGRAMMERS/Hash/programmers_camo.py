def solution(clothes):
    answer = 1
    category = {}
    for clothe in clothes:
        if clothe[1] not in category:
            category[clothe[1]] = 1
        else:
            category[clothe[1]] += 1
    for c in category:
        answer *= category[c] + 1
    return answer - 1

print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))