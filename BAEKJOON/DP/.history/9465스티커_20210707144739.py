def getMaxPoint(pattern, cache, sticker, n):
    """
    sticker에서, 마지막 열 스티커가 pattern의 형태로 제거되었을 때,
    0부터 n열까지의 최대 점수를 리턴
    """
    if cache[n] != -1: #캐시에 이전에 계산한 결과가 있다.
        return cache[n]
    
    if n < 0:
        pass
    else:
        if n >= 3:
            cache[n] = max(getMaxPoint(pattern, cache, sticker, n-2), getMaxPoint(pattern, cache, sticker, n-3)) + sticker[pattern][n]
        elif n == 2:
            cache[n] = max( getMaxPoint(pattern, cache, sticker, n-2), sticker[int(not pattern)][0] ) + sticker[pattern][n]
        elif n == 1:
            cache[n] = sticker[int(not pattern)][0] + sticker[pattern][n]
        elif n == 0:
            cache[n] = sticker[pattern][n]
        return cache[n]
   


T = int(input())
for i in range(T):
    n = int(input())
    row1 = input().split(" ")
    row2 = input().split(" ")
    sticker = [[int(point) for point in row1], [int(point) for point in row2]]

    cache = [-1 for j in range(n)]
    # 패턴A는 마지막 열에서 상단에 있는 스티커를 뗴어낸 경우.
    patternA_max = getMaxPoint(0, cache, sticker, n-1)
    print(patternA_max)

