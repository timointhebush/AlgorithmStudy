def solution(n, edge):
    visited = [False for node in range(n)]
    graph = makeGraph(n, edge)
    current_level = [0]
    visited[0] = True
    while True:
        next_level = []
        for current_node in current_level:
            for connected_node in graph[current_node]:
                if visited[connected_node] == False:
                    visited[connected_node] = True
                    next_level.append(connected_node)
        if next_level == []:
            break
        current_level = next_level
    return len(current_level)

def makeGraph(n, edge):
    graph = [[] for _ in range(n)]
    for e in edge:
        graph[e[0]-1].append(e[1]-1)
        graph[e[1]-1].append(e[0]-1)
    return graph

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))