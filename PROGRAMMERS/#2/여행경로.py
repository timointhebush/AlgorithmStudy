from collections import defaultdict


def solution(tickets):
    # graph 생성
    graph = defaultdict(list)
    for depart, arrive in tickets:
        graph[depart].append(arrive)

    # graph 정렬, visited 생성
    visited = {}
    for depart in graph.keys():
        graph[depart].sort()
        visited[depart] = [False for _ in range(len(graph[depart]))]

    # check
    print("graph: ", graph)
    print("visited: ", visited)

    # dfs함수 정의
    def dfs(depart, route):
        if len(route) == len(tickets) + 1:
            return route
        for i, arrive in enumerate(graph[depart]):
            if visited[depart][i] == False:
                visited[depart][i] = True
                tmp_route = route.copy()
                tmp_route.append(arrive)
                answer = dfs(arrive, tmp_route)

                visited[depart][i] = False
                if answer:
                    return answer

    return dfs("ICN", ["ICN"])


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
