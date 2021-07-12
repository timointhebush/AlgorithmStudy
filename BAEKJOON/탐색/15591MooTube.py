def getMinDistance(distance, set_not_grouped):
    min_dist = list(set_not_grouped)[0]
    for vertex in set_not_grouped:
        if distance[vertex] < distance[min_dist]:
            min_dist = vertex
    return min_dist

tmp = input().split(" ")
N, Q = int(tmp[0]), int(tmp[1])
tree = [{} for i in range(N+1)] #영상 번호와 index를 동일하게 하기 위해 N+1개
# distance[a][b] -> 시작 정점이 a로 최소 신장 트리를 형성해 나갈때, 
# 형성 그룹에서부터 정점 b까지 최소 거리 
# distance[a][0] -> 0열은 시작 정점 a로 최소 신장 트리를 형성한적이 있는지에 대한 데이터
# 만약 inf가 아니라면 형성한 적이 있음.
distance = [[float('inf') for i in range(N+1)] for j in range(N+1)]

for i in range(N-1):
    tmp = input().split(" ")
    p, q, r = int(tmp[0]), int(tmp[1]), int(tmp[2])
    tree[p][q] = r
    tree[q][p] = r

questions = []
for i in range(Q):
    tmp = input().split(" ")
    K, V = int(tmp[0]), int(tmp[1])
    questions.append((K, V))



for K, V in questions:
    ans = 0
    if distance[V][0] == float("inf") : #형성 한적 없음
        distance[V][0] = 0
        vertexes = set([i for i in range(1, N+1)]) 
        grouped_v = set()
        distance[V][V] = 0
        while len(vertexes) != len(grouped_v):
            v = getMinDistance(distance[V], vertexes - grouped_v)
            grouped_v.add(v)
            for connected, w in tree[v].items():
                if connected not in grouped_v:
                    if distance[V][v] != 0:
                        distance[V][connected] = min(w, distance[V][v])
                    else:
                        distance[V][connected] = w
    else: #형성 있음
        pass

    for i in range(1, N+1):
        if K <= distance[V][i]:
            ans += 1
    print(ans)
