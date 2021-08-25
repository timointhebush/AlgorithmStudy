def solution(n, s, a, b, fares):
    answer = 0
    graph = getGraph(n, fares)
    # s - 합승, 합승 -a, 합승- b -> 각 최단거리
    cand = {}
    shortestSList = getShortest(s, graph, n)
    for shareP in range(1, n+1):
        shortestList = getShortest(shareP, graph, n)
        shortest = shortestSList[shareP] + shortestList[a] + shortestList[b]
        cand[shareP] = shortest
    # print(cand)
    return min(cand.values())

def getGraph(n, fares):
    graph = { i:{} for i in range(1, n+1) }
    for fare in fares:
        a, b, length = fare[0], fare[1], fare[2]
        graph[a][b] = length
        graph[b][a] = length
    return graph

def getShortest(start, graph, n):
    d = [float('inf') for _ in range(n+1)]
    d[start] = 0
    V = set( [i for i in range(1, n+1)] )
    S = set()
    while S != V:
        minV = extractMin(V-S, d)
        S.add(minV)
        for connected in graph[minV]:
            if d[connected] > graph[minV][connected] + d[minV]:
                d[connected] = graph[minV][connected] + d[minV]
    return d

def extractMin(notVisited, d):
    minimun = list(notVisited)[0]
    for v in list(notVisited):
        if d[v] < d[minimun]:
            minimun = v
    return minimun

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))