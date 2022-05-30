import heapq as hq

def solution(jobs):
    answer = 0
    current_ms = 0
    jobs = sorted([[x[1], x[0]] for x in jobs], key=lambda x:(x[1], x[0]))
    requested = []
    n = len(jobs)

    while True:
        #현재시간인 current_ms에 따라 요청받은 작업을 고르는 부분
        if len(jobs) != 0:
            for_pop = []
            for idx, job in enumerate(jobs):
                if job[1] <= current_ms:
                    hq.heappush(requested, job)
                    for_pop.append(idx)
                else:
                    break
            for idx in for_pop:
                jobs.pop(0)
        
        if len(requested) == 0:
            if len(jobs) != 0: #만약 현재 시간까지 요청받은 작업이 없다면, 
                #가장 가까운 시기에 요창받은 작업으로 이동, 이를 리스트에 추가, 현재 시간도 변경
                hq.heappush(requested, jobs.pop(0))
                current_ms = requested[0][1]
            else: #모든 작업을 완료했을 때.
                break
        #요청 받은 작업들 중, 어떤 것을 수행할 지 고르는 부분
        #수행 시간이 가장 짧고, 만약 수행 시간이 같다면 요청 시간이 빠른 것을 선택.

        exe = hq.heappop(requested)
        #총 시간을 계산하고, 현재 시간을 변경해줌.
        answer += (current_ms - exe[1]) + exe[0]
        current_ms += exe[0]
    
    return int(answer/n)

print(solution([[0, 10], [2, 10], [9, 10], [15, 2]]), 14)
print(solution([[0, 10], [2, 12], [9, 19], [15, 17]]), 25)
print(solution([[0, 3], [1, 9], [2, 6]]), 9)
print(solution([[0, 1]]), 1)
print(solution([[1000, 1000]]), 1000)
print(solution([[0, 1], [0, 1], [0, 1]]), 2)
print(solution([[0, 1], [0, 1], [0, 1], [0, 1]]), 2)
print(solution([[0, 1], [1000, 1000]]), 500)
print(solution([[100, 100], [1000, 1000]]), 500)
print(solution([[10, 10], [30, 10], [50, 2], [51, 2]]), 6)
print(solution([[0, 3], [1, 9], [2, 6], [30, 3]]), 7)
