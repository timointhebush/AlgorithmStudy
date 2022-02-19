def solution(n, costs):
    d = [float('inf') for i in range(n)]
    d[0] = 0
    Q = {i for i in range(n)} #Q는 아직 연결되지 않은 노드들의 집합
    answer = 0
    while len(Q) != 0:
        u = deleteMin(Q, d)
        answer += d[u]
        #정점 u와 인접한 정점을 찾는다
        for line in costs:
            for idx in range(2):
                if line[idx] == u: #정점 u와 연결되어있음]
                    if line[1-idx] in Q and line[2] < d[line[1-idx]]:
                        d[line[1-idx]] = line[2]
    return answer

def deleteMin(Q, d):
    minWeight = float('inf')
    minNode = None
    for node in Q:
        if d[node] < minWeight:
            minNode = node
            minWeight = d[node]
    Q.remove(minNode)
    return minNode

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))