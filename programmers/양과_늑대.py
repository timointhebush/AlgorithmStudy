from collections import defaultdict
import copy

graph = None
is_wolf = None
answer = 0


def solution(info, edges):
    global graph, is_wolf, answer
    graph = defaultdict(list)
    is_wolf = info
    for parent, child in edges:
        graph[parent].append(child)
        graph[child].append(parent)
    dfs(0, set(), {0: 0, 1: 0}, [])
    return answer


def dfs(current_node, visited, animal, visitable_nodes):
    global graph, is_wolf, answer
    visited.add(current_node)
    animal[is_wolf[current_node]] += 1
    if animal[0] <= animal[1]:
        return
    if answer < animal[0]:
        answer = animal[0]
    nxt_visitable_nodes = []
    connected_nodes = graph[current_node]
    for node in (visitable_nodes + connected_nodes):
        if node not in visited and node != current_node:
            nxt_visitable_nodes.append(node)
    for nxt_node in nxt_visitable_nodes:
        dfs(nxt_node, copy.deepcopy(visited), copy.deepcopy(animal), nxt_visitable_nodes)


# print(solution(	[0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))
# print(solution([0, 0], [[0, 1]]))