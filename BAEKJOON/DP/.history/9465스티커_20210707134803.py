def getMaxPoint(pattern, cache, sticker, n):
    """
    sticker에서, 마지막 열 스티커가 pattern의 형태로 제거되었을 때,
    0부터 n열까지의 최대 점수를 리턴
    """
    
    return 0


T = int(input())
for i in range(T):
    n = int(input())
    row1 = input().split(" ")
    row2 = input().split(" ")
    sticker = [[int(point) for point in row1], [int(point) for point in row2]]

    cache = [-1 for j in range(n)]
    # 패턴A는 마지막 열에서 상단에 있는 스티커를 뗴어낸 경우.
    patternA_max = getMaxPoint(pa)

