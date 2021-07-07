# 백준 제출 시
#import sys
#sys.setrecursionlimit(10**6)

def getMaxPoint(pattern, cache, sticker, n):
    """
    sticker에서, 마지막 열 스티커가 pattern의 형태로 제거되었을 때,
    0부터 n열까지의 최대 점수를 리턴
    """
    if cache[pattern][n] != -1: #캐시에 이전에 계산한 결과가 있다.
        return cache[pattern][n]
    if n < 0:
        pass
    else:
        p1, p2 = getRightPattern(pattern)
        if n >= 1:
            cache[pattern][n] = max( getMaxPoint(p1, cache, sticker, n-1), getMaxPoint(p2, cache, sticker, n-1) ) + sticker[pattern][n]
        else: # n == 0
            cache[pattern][n] = sticker[pattern][n]
        return cache[pattern][n]

def getRightPattern(pattern):
    if pattern == 0:
        return (1, 2)
    elif pattern == 1:
        return (0, 2)
    else: # pattern == 2
        return (0, 1)


T = int(input())
for i in range(T):
    n = int(input())
    row1 = input().split(" ")
    row2 = input().split(" ")
    sticker = [[int(point) for point in row1], [int(point) for point in row2], [0 for j in range(n)]]
    
    # 패턴A는 마지막 열에서 상단에 있는 스티커를 뗴어낸 경우.
    cache = [[-1 for j in range(n)], [-1 for j in range(n)], [-1 for j in range(n)]]
    patternA_max = getMaxPoint(0, cache, sticker, n-1)

    cache = [[-1 for j in range(n)], [-1 for j in range(n)], [-1 for j in range(n)]]
    patternB_max = getMaxPoint(1, cache, sticker, n-1)

    print(max(patternA_max, patternB_max))

