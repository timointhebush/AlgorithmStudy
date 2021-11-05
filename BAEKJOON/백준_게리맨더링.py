from itertools import combinations
from collections import deque


def solution():
    global N, graph, population
    N = int(input())
    population = list(map(int, input().split(" ")))
    graph = {}
    for i in range(N):
        tmp = list(map(int, input().split(" ")))
        graph[i] = list(map(lambda x: x - 1, tmp[1:]))
    diff_cand = []
    # 한 선거구 경우의 수.
    cases = make_cases()
    for case in cases:
        district_A = set(case)
        district_B = set(range(N)) - set(case)
        districts = [district_A, district_B]
        if check_connectivity(districts):
            diff_cand.append(get_pop_diff(districts))
    return min(diff_cand) if len(diff_cand) != 0 else -1


def make_cases():
    district = range(N)
    cases = []
    for i in range(1, N // 2 + 1):
        cases += combinations(district, i)
    return cases


def check_connectivity(districts):
    district_A, district_B = districts
    visited_n_A = bfs(district_A)
    visited_n_B = bfs(district_B)
    if visited_n_A + visited_n_B == N:
        return True
    else:
        return False
    # for dist in districts:
    #     for node in dist:
    #         connect_list = set(graph[node])
    #         if connect_list & (dist - set([node])) == set():
    #             return False
    # return True


def bfs(district):
    list_district = list(district)
    visited = set([list_district[0]])
    queue = deque([list_district[0]])
    while len(queue) != 0:
        start = queue.popleft()
        connected_nodes = graph[start]
        for c_node in connected_nodes:
            if c_node not in visited and c_node in district:
                visited.add(c_node)
                queue.append(c_node)
    return len(visited)


def get_pop_diff(districts):
    pop_A, pop_B = 0, 0
    for dist in districts[0]:
        pop_A += population[dist]
    for dist in districts[1]:
        pop_B += population[dist]
    return abs(pop_A - pop_B)


print(solution())
