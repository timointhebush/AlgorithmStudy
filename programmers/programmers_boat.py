def solution(people, limit):
    people.sort()
    boat = 0
    answer = 0
    small = 0
    big = len(people) - 1
    while big >= small:
        boat += people[big]
        while boat + people[small] <= limit and small < big:
            boat += people[small]
            small += 1
        answer += 1
        big -= 1
        boat = 0
    return answer

print(solution([70, 50, 80, 50], 100))