#동기화 안한 버전
import heapq as hq

def solution(operations):
    minHeap, maxHeap = [], []
    for operation in operations:
        if operation[0] == "I":
            num = int(operation.split()[1])
            hq.heappush(minHeap, num)
            hq.heappush(maxHeap, (-num, num))
        elif operation == "D 1":
            if maxHeap != []:
                hq.heappop(maxHeap)[1]
                if maxHeap == [] or maxHeap[0][1] < minHeap[0]:
                    minHeap, maxHeap = [], []
        else:
            if minHeap != []:
                hq.heappop(minHeap)
                if minHeap == [] or maxHeap[0][1] < minHeap[0]:
                    minHeap, maxHeap = [], []
    if minHeap == [] and maxHeap == []:
        return [0,0]
    else:
        return [hq.heappop(maxHeap)[1], hq.heappop(minHeap)]

print(solution(['I 7','I 5','I -5','D -1']))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))