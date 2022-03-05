import sys

def solution():
    N, K = tuple(map(int, sys.stdin.readline().split(" ")))
    items = []
    max_v = 0
    sum_w = 0
    for _ in range(N):
        W, V = tuple(map(int, sys.stdin.readline().split(" ")))
        if V > max_v:
            max_v = V
        sum_k += W
        items.append((W, V))
    items = sorted(items)
    print(items)
    left, right = 0, max_v
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        bag_w = 0
        bag_v = 0
        for W, V in items:
            if V < mid:

            bag_w += W
            bag_v += V

    

solution()
