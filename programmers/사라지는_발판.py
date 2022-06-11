dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
R, C = 0, 0

block = [[0 for _ in range(5)] for _ in range(5)]
visited = [[0 for _ in range(5)] for _ in range(5)]


def is_out(r, c):
    return r < 0 or r >= R or c < 0 or c >= C


def get_left_move(cur_r, cur_c, op_r, op_c):
    global visited, block
    if visited[cur_r][cur_c]:
        return 0
    result = 0
    for dir in range(4):
        nxt_r = cur_r + dr[dir]
        nxt_c = cur_c + dc[dir]
        if is_out(nxt_r, nxt_c) or visited[nxt_r][nxt_c] or block[nxt_r][nxt_c] == 0:
            continue
        visited[cur_r][cur_c] = 1
        value = get_left_move(op_r, op_c, nxt_r, nxt_c) + 1
        visited[cur_r][cur_c] = 0

        if result % 2 == 0 and value % 2 == 1:
            result = value
        elif result % 2 == 0 and value % 2 == 0:
            result = max(result, value)
        elif result % 2 == 1 and value % 2 == 1:
            result = min(result, value)

    return result


def solution(board, aloc, bloc):
    global R, C
    R, C = len(board), len(board[0])
    for r in range(R):
        for c in range(C):
            block[r][c] = board[r][c]
    a_r, a_c = aloc
    b_r, b_c = bloc
    return get_left_move(a_r, a_c, b_r, b_c)


print(solution(	[[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]))