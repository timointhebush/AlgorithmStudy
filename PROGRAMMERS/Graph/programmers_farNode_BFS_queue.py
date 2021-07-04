def solution(n, edge):
    visited = [False for node in range(n)]
    distance = [0 for _ in range(n)]
    graph = makeGraph(n, edge)
    queue = [0]
    visited[0] = True
    while queue:
        current_node = queue.pop(0)
        for connected in graph[current_node]:
            if visited[connected] == False:
                visited[connected] = True
                distance[connected] += distance[current_node] + 1
                queue.append(connected)
    max_distance = max(distance)
    return distance.count(max_distance)

def makeGraph(n, edge):
    graph = [[] for _ in range(n)]
    for e in edge:
        graph[e[0]-1].append(e[1]-1)
        graph[e[1]-1].append(e[0]-1)
    return graph

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))