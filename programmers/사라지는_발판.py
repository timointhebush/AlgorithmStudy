dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = 0, 0
game_board = []


def is_in(r, c):
    return 0 <= r < R and 0 <= c < C


def is_finished(r, c):
    for dir in range(4):
        nxt_r = r + dr[dir]
        nxt_c = c + dc[dir]
        if is_in(nxt_r, nxt_c) and game_board[nxt_r][nxt_c]:
            return False
    return True


def solution(board, aloc, bloc):
    global game_board, R, C
    game_board = board
    R = len(board)
    C = len(board[0])
    return solve(aloc[0], aloc[1], bloc[0], bloc[1])[1]


def solve(cur_r, cur_c, opp_r, opp_c):
    """
    cur의 턴일 때, 최선의 플레이 시 (승리 여부, 최적 플레이 시 턴 수) 반환
    """
    global game_board
    if is_finished(cur_r, cur_c):
        return False, 0
    if cur_r == opp_r and cur_c == opp_c:
        return True, 1

    can_win = False
    min_turn = float("inf")
    max_turn = 0
    for dir in range(4):
        nxt_r = cur_r + dr[dir]
        nxt_c = cur_c + dc[dir]
        if not is_in(nxt_r, nxt_c) or not game_board[nxt_r][nxt_c]:
            continue
        game_board[cur_r][cur_c] = 0
        result = solve(opp_r, opp_c, nxt_r, nxt_c)
        game_board[cur_r][cur_c] = 1

        if not result[0]:
            # opp가 패배
            can_win = True
            min_turn = min(min_turn, result[1])
        elif not can_win:
            max_turn = max(max_turn, result[1])
    turn = min_turn if can_win else max_turn
    return can_win, turn + 1



print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]))