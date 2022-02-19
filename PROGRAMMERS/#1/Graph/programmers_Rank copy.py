def solution(n, results):
    answer = 0
    win_against, lose_against = {}, {}
    for player in range(1, n+1):
        win_against[player] = set()
        lose_against[player] = set()
    for result in results:
        winner, loser = result[0], result[1]
        win_against[loser].add(winner)
        lose_against[winner].add(loser)
    for player in range(1, n+1):
        for winner in win_against[player]:
            lose_against[winner].update(lose_against[player])
        for loser in lose_against[player]:
            win_against[loser].update(win_against[player])
    for player in range(1, n+1):
        if len(win_against[player]) + len(lose_against[player]) == n-1:
            answer += 1
    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
print(solution(5, [[3, 5], [4, 2], [4, 5], [5, 1], [5, 2]]))
print(solution(8, [[1, 2], [2, 3], [3, 4], [5, 6], [6, 7], [7, 8]] ))