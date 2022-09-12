dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

game_board = []
R = 0
C = 0


def solution(board, aloc, bloc):
    global game_board, R, C
    game_board = board
    R, C = len(board), len(board[0])
    _, total_move = get_cur_is_win_and_total_move(tuple(aloc), tuple(bloc))
    return total_move


def get_cur_is_win_and_total_move(cur, opp):
    global game_board
    if not is_movable(cur):
        return False, 0
    if cur == opp:
        return True, 1

    cur_winnable = False
    min_total_move = float('inf')
    max_total_move = 0
    for i in range(4):
        nxt_cur = (cur[0] + dr[i], cur[1] + dc[i])
        if not can_move(nxt_cur):
            continue
        game_board[cur[0]][cur[1]] = 0
        opp_is_win, total_move_since_now = get_cur_is_win_and_total_move(opp, nxt_cur)
        game_board[cur[0]][cur[1]] = 1

        if not opp_is_win:
            cur_winnable = True
            min_total_move = min(min_total_move, total_move_since_now)
        elif not cur_winnable:
            max_total_move = max(max_total_move, total_move_since_now)
    total_move = min_total_move if cur_winnable else max_total_move
    return cur_winnable, total_move + 1


def is_in(player):
    return 0 <= player[0] < R and 0 <= player[1] < C


def can_move(coord):
    return is_in(coord) and game_board[coord[0]][coord[1]]


def is_movable(cord):
    for i in range(4):
        nxt_cord = (cord[0] + dr[i], cord[1] + dc[i])
        if can_move(nxt_cord):
            return True
    return False


if __name__ == "__main__":
    # print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]))
    print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1, 0], [1, 2]))
