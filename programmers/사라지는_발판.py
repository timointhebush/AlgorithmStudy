dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
visited = []
game_board = []


def solution(board, aloc, bloc):
    global visited, game_board
    game_board = board
    visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    return solve(aloc[0], aloc[1], bloc[0], bloc[1])


def solve(cur_r, cur_c, opp_r, opp_c):
    if visited[cur_r][cur_c]:
        return 0
    cur_result = 0
    for dir in range(4):
        nxt_cur_r, nxt_cur_c = cur_r + dr[dir], cur_c + dc[dir]
        visited[nxt_cur_r][nxt_cur_c] = 1
        nxt_result = solve(opp_r, opp_c, nxt_cur_r, nxt_cur_c) + 1
        visited[nxt_cur_r][nxt_cur_c] = 0
        if cur_result % 2 == 0 and nxt_result % 2 == 1:
            cur_result = nxt_result
        elif cur_result % 2 == 1 and nxt_result % 2 == 0:
            cur_result = min(nxt_result, cur_result)
        elif cur_result % 2 == 0 and nxt_result % 2 == 0:
            cur_result = max(nxt_result, cur_result)
        return cur_result