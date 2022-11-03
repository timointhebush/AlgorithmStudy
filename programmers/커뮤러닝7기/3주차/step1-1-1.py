import heapq


def get_mixed_scoville(first, second):
    return first + (second * 2)


def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        if first == 0 and second == 0:
            return -1
        mix = get_mixed_scoville(first, second)
        answer += 1
        heapq.heappush(scoville, mix)
    return answer


if __name__ == "__main__":
    print(solution([1, 2, 3, 9, 10, 12], 7))
