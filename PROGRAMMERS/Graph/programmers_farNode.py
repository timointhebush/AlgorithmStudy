def solution(n, edge):
    distance = {node:float('inf') for node in range(1, n+1)}
    not_visited_node = [node for node in range(1, n+1)]
    distance[1] = 0
    graph = makeGraph(n, edge)
    while len(not_visited_node) != 0:
        minNode = getMinDistanceNode(distance, not_visited_node)
        not_visited_node.remove(minNode)
        connected = graph[minNode]
        for c in connected:
            if distance[c] > distance[minNode] + 1:
                distance[c] = distance[minNode] + 1
    return getAnswer(distance)

def makeGraph(n, edge):
    graph = [[] for _ in range(n+1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    return graph

def getMinDistanceNode(distance, not_visited_node):
    minNode = not_visited_node[0]
    for node in not_visited_node:
        if distance[node] < distance[minNode]:
            minNode = node
    return minNode

def getAnswer(distance):
    max_distance = distance[max(distance)]
    num = 0
    for d in distance.values():
        if max_distance == d:
            num += 1
    return num

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))