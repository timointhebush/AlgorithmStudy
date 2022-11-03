import heapq
import heapq as hq


def solution(t, k, study, pstudy):
    study_i = [[hour, i] for i, hour in enumerate(study)]
    pstudy_i = [[hour, i] for i, hour in enumerate(pstudy)]
    hq.heapify(study_i)
    hq.heapify(pstudy_i)

    answer = 0
    tmp_t = 0
    studied_i = set()

    for _ in range(k):
        hour, i = heapq.heappop(pstudy_i)
        if tmp_t + hour >= t:
            return answer
        tmp_t += hour
        studied_i.add(i)
        answer += 1

    while len(study_i) > 0:
        hour, i = heapq.heappop(study_i)
        if i in studied_i:
            continue
        if tmp_t + hour >= t:
            return answer
        tmp_t += hour
        studied_i.add(i)
        answer += 1
    return answer


if __name__ == "__main__":
    # print(solution(100, 3, [90, 100, 90, 80, 40, 50], [1, 2, 3, 10, 20, 30]))
    print(solution(100, 1, [10], [4]))