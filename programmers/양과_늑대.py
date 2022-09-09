from collections import defaultdict
import copy

graph = defaultdict(list)
is_wolf = []
answer = 0


def solution(info, edges):
    global graph, is_wolf
    is_wolf = info
    visited = [False for _ in range(len(info))]
    for e in edges:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    dfs(0, 0, 0, [], visited)
    return answer


def dfs(node, sheep_num, wolf_num, prev_nodes, visited):
    global answer
    if not visited[node]:
        if is_wolf[node]:
            wolf_num += 1
        else:
            sheep_num += 1
            answer = max(answer, sheep_num)
        visited[node] = True

    if wolf_num >= sheep_num:
        return

    prev_nodes.extend(graph[node])
    for nxt_node in prev_nodes:
        if not visited[nxt_node]:
            nxt_prev_nodes = [prev_node for prev_node in prev_nodes if prev_node != nxt_node and not visited[prev_node]]
            dfs(nxt_node, sheep_num, wolf_num, nxt_prev_nodes, copy.deepcopy(visited))


if __name__ == "__main__":
    print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
                   [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))
