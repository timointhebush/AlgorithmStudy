def solution(tickets):
    answer = []
    tickets.sort(key = lambda x:(x[0], x[1]))
    ICNidx = []
    visited = [False for i in range(len(tickets))]
    for idx in range(len(tickets)):
        if tickets[idx][0] == 'ICN':
            ICNidx.append(idx)
    for rootIdx in ICNidx:
        if DFS(tickets, rootIdx, answer, 0, visited):
            break
    return changeAnswer(answer)

def DFS(tickets, parentIdx, answer, level, visited):
    answer.append(tickets[parentIdx])
    visited[parentIdx] = True
    result = False
    if level == len(tickets)-1:
        result = True
    else:
        for nextIdx in range(len(tickets)):
            if visited[nextIdx] == False and tickets[nextIdx][0] == tickets[parentIdx][1]:
                result = DFS(tickets, nextIdx, answer, level+1, visited)
        if result == False:
            answer.pop()
            visited[parentIdx] = False
    return result

def changeAnswer(answer):
    n = len(answer)
    tmp = []
    for i in range(n):
        if i == n-1:
            for j in range(2):
                tmp.append(answer[i][j])
        else:
            tmp.append(answer[i][0])
    return tmp

print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]))
print(solution([['ICN','A'],['ICN','A'],['A','ICN']] ))