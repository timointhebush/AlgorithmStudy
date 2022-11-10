dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def solution(rows, columns, max_virus, queries):
    board = [[0 for _ in range(columns)] for _ in range(rows)]
    for r, c in queries:
        is_multiplied = [[False for _ in range(columns)] for _ in range(rows)]
        multiply_germ(r - 1, c - 1, board, max_virus, is_multiplied)
    return board


def multiply_germ(r, c, board, max_virus, is_multiplied):
    num_germ = board[r][c]
    if num_germ < max_virus:
        board[r][c] += 1
    else:
        for dir in range(4):
            nr, nc = r + dr[dir], c + dc[dir]
            if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and not is_multiplied[nr][nc]:
                is_multiplied[nr][nc] = True
                multiply_germ(nr, nc, board, max_virus, is_multiplied)


if __name__ == "__main__":
    print(solution(3, 4, 2, [[3, 2], [3, 2], [2, 2], [3, 2], [1, 4], [3, 2], [2, 3], [3, 1]]))
