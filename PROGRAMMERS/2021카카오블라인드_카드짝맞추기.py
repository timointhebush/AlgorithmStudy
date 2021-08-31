from collections import deque


def solution(board, r, c):
    n = len(board)
    cards = set()
    new_board = [[7 for _ in range(n + 2)] for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
            if board[i][j] != 0:
                cards.add((i, j))
    # print(get_next_moves(r + 1, c + 1, new_board))
    queue = deque([(r + 1, c + 1, 0, [])])
    visited = [(r + 1, c + 1, 0, [])]
    completed_cards = set()
    while queue:
        r, c, num, turned = queue.popleft()
        if set(turned) == cards:
            return num
        next_moves = get_next_moves(r, c, new_board)
        for nr, nc in next_moves:
            if (r, c) == (nr, nc):
                n_turned = turned


def get_next_moves(r, c, new_board):
    next_moves = set()
    if new_board[r][c] != 0:
        next_moves.add((r, c))
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r + dr, c + dc
        if new_board[nr][nc] != 7:
            next_moves.add((nr, nc))

    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r + dr, c + dc
        while new_board[nr][nc] not in [1, 2, 3, 4, 5, 6]:
            if new_board[nr][nc] == 7:
                nr, nc = nr - dr, nc - dc
                break
            else:
                nr, nc = nr + dr, nc + dc
        next_moves.add((nr, nc))
    return next_moves


print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0))
