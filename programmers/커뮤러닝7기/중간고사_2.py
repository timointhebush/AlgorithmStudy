from collections import deque


def solution(people, tshirts):
    reversed_people_q = deque(sorted(people, reverse=True))
    reversed_tshirts_q = deque(sorted(tshirts, reverse=True))
    answer = 0
    while reversed_people_q and reversed_tshirts_q:
        people_size = reversed_people_q.popleft()
        if people_size > reversed_tshirts_q[0]:
            continue
        reversed_tshirts_q.popleft()
        answer += 1
    return answer