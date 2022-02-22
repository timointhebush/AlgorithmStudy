from collections import defaultdict


def solution(tickets):
    graph = defaultdict(list)
    visited = defaultdict(list)
    for depart, arrive in tickets:
        graph[depart].append(arrive)

    # 정렬
    for depart in graph.keys():
        graph[depart].sort()
        visited[depart] = [False for _ in range(len(graph[depart]))]
    print("graph: ", graph)
    print("visited: ", visited)

    def dfs(depart, route):
        if len(route) == len(tickets) + 1:
            return route

        for i, arrive in enumerate(graph[depart]):
            if visited[depart][i] == False:
                visited[depart][i] = True
                tmp_route = route.copy()
                tmp_route.append(arrive)

                ret = dfs(arrive, tmp_route)

                visited[depart][i] = False

                if ret:
                    return ret

    answer = dfs("ICN", ["ICN"])
    return answer


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
