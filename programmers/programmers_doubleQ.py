import heapq as hq

def solution(operations):
    minHeap, maxHeap = [], []
    for operation in operations:
        if operation[0] == "I":
            num = int(operation.split()[1])
            hq.heappush(minHeap, num)
            hq.heappush(maxHeap, (-num, num))
        elif len(minHeap) != 0:
            if operation == "D 1":
                maxNum = hq.heappop(maxHeap)[1]
                minHeap.remove(maxNum)
            else:
                minNum = hq.heappop(minHeap)
                maxHeap.remove((-minNum, minNum))
    if len(maxHeap) != 0:
        return [hq.heappop(maxHeap)[1], hq.heappop(minHeap)]
    else:
        return [0,0]

print(solution(['I 7','I 5','I -5','D -1']))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))