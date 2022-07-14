graph = []
visited = []
values = []
answer = 0


def solution(a, edges):
    if sum(a) != 0:
        return -1

    global graph, visited, values
    values = a
    graph = [[] for _ in range(len(a))]
    visited = [0 for _ in range(len(a))]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    visited[0] = 1
    dfs(0)
    return answer


def dfs(node):
    global answer, visited
    now_value = values[node]
    visited[node] = 1

    con_nodes = graph[node]
    for con_node in con_nodes:
        if not visited[con_node]:
            now_value += dfs(con_node)
    answer += abs(now_value)
    return now_value


print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]]))