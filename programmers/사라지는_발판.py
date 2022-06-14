dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

game_board = []
visited = []


def solution(board, aloc, bloc):
    global game_board, visited
    game_board = board
    visited = [[0] * len(board[0]) for _ in range(len(board))]
    print(visited)
    return get_sum_of_move(aloc[0], aloc[1], bloc[0], bloc[1])


def get_sum_of_move(cur_r, cur_c, opp_r, opp_c):
    global game_board, visited
    cur_sum_of_move = 0
    if visited[cur_r][cur_c]:
        return cur_sum_of_move
    for dir in range(4):
        nxt_cur_r, nxt_cur_c = cur_r + dr[dir], cur_c + dc[dir]
        if not is_movable(nxt_cur_r, nxt_cur_c):
            continue
        visited[cur_r][cur_c] = 1
        future_sum_of_move = get_sum_of_move(opp_r, opp_c, nxt_cur_r, nxt_cur_c) + 1
        visited[cur_r][cur_c] = 0
        if not is_winner(cur_sum_of_move) and is_winner(future_sum_of_move):
            cur_sum_of_move = future_sum_of_move
        elif not is_winner(cur_sum_of_move) and not is_winner(future_sum_of_move):
            cur_sum_of_move = max(cur_sum_of_move, future_sum_of_move)
        elif is_winner(cur_sum_of_move) and is_winner(future_sum_of_move):
            cur_sum_of_move = min(cur_sum_of_move, future_sum_of_move)
    return cur_sum_of_move


def is_movable(r, c):
    return 0 <= r < len(game_board) and 0 <= c < len(game_board[0])\
           and game_board[r][c] and not visited[r][c]


def is_winner(move):
    return move % 2 == 1


print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]))