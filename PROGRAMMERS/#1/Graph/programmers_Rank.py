def solution(n, results):
    answer = 0
    rank = [None for _ in range(n)]
    graph = makeGraphMatrix(n, results)
    answer += selectCertainPlayerRank(graph, rank)
    answer += getRestRank(graph, rank, n)
    return answer

def makeGraphMatrix(n, results):
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for game in results:
        graph[game[0]-1][game[1]-1] = 1
        graph[game[1]-1][game[0]-1] = -1
    return graph

def selectCertainPlayerRank(graph, rank):
    certain_player_num = 0
    for player, games in enumerate(graph):
        count_zero = 0
        count_minus_one = 0
        for result in games:
            if result == 0:
                count_zero += 1
            if result == -1:
                count_minus_one += 1
        if count_zero == 1:
            certain_player_num += 1
            rank[count_minus_one] = player
    return(certain_player_num)

def getRestRank(graph, rank, n):
    possible_num = 0
    for r, player in enumerate(rank):
        if player == None:
            if r == 0:
                if rank[1] != None:
                    for result in graph[rank[1]]:
                        if result == -1:
                            possible_num += 1
            elif r == n-1:
                if rank[n-2] != None:
                    for result in graph[rank[n-2]]:
                        if result == 1:
                            possible_num += 1
            else:
                if rank[r-1] != None and rank[r+1] != None:
                    for opponent, result1 in enumerate(graph[rank[r-1]]):
                        if result1 == 1 and graph[rank[r+1]][opponent] == -1:
                            possible_num += 1
    return possible_num


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
print(solution(5, [[3, 5], [4, 2], [4, 5], [5, 1], [5, 2]]))
print(solution(8, [[1, 2], [2, 3], [3, 4], [5, 6], [6, 7], [7, 8]] ))