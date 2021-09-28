import heapq


def solution(a):
    answer = 2
    n = len(a)
    balloons = [(b, i) for i, b in enumerate(a)]
    left_heap, right_heap = balloons[:1], balloons[2:]
    heapq.heapify(left_heap)
    heapq.heapify(right_heap)
    NUM, IDX = 0, 1
    for i in range(1, n - 1):
        target = a[i]
        num = 0
        if target == right_heap[0][NUM]:
            heapq.heappop(right_heap)
            while i < right_heap[0][IDX]:
                heapq.heappop(right_heap)
        if target < left_heap[0][NUM]:
            num += 1
        if target < right_heap[0][NUM]:
            num += 1
        if num >= 1:
            answer += 1
        heapq.heappush(left_heap, (target, i))
    return answer


# print(solution([9, -1, -5]))
print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))
