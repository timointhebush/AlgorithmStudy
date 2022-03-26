import heapq as hq


def solution(N, nums):
    min_heap, max_heap = [], []
    hq.heappush(max_heap, -nums[0])
    print(-max_heap[0])
    for i in range(2, N + 1):
        # push
        num = nums[i - 1]
        if num > -max_heap[0]:
            hq.heappush(min_heap, num)
        else:
            hq.heappush(max_heap, -num)
        # 개수 조정
        if i % 2 == 0 and len(max_heap) != len(min_heap):
            if len(max_heap) > len(min_heap):
                from_heap, to_heap = max_heap, min_heap
            else:
                from_heap, to_heap = min_heap, max_heap
            while len(max_heap) != len(min_heap):
                hq.heappush(to_heap, -hq.heappop(from_heap))
        elif i % 2 != 0 and len(max_heap) != len(min_heap) + 1:
            if len(max_heap) > len(min_heap) + 1:
                from_heap, to_heap = max_heap, min_heap
            else:
                from_heap, to_heap = min_heap, max_heap
            while len(max_heap) != len(min_heap) + 1:
                hq.heappush(to_heap, -hq.heappop(from_heap))
        print(-max_heap[0])


if __name__ == "__main__":
    N = int(input())
    nums = []
    for i in range(N):
        nums.append(int(input()))
    solution(N, nums)
