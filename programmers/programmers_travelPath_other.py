#dafaultdict이라는 자료형을 사용해서 효율적으로 풀이할 수 있었다.

from collections import defaultdict 

def dfs(graph, N, key, footprint):
    if len(footprint) == N + 1:
        return footprint
    for idx, country in enumerate(graph[key]):
        graph[key].pop(idx)
        tmp = footprint[:]
        tmp.append(country)
        ret = dfs(graph, N, country, tmp)
        graph[key].insert(idx, country)
        if ret:
            return ret

def solution(tickets):
    answer = []
    graph = defaultdict(list)
    N = len(tickets)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
        graph[ticket[0]].sort()
    answer = dfs(graph, N, "ICN", ["ICN"])
    return answer

print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]))
print(solution([['ICN','A'],['ICN','A'],['A','ICN']] ))