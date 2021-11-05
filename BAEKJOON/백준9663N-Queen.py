def solution():
    global board, N, cnt
    N = int(input())
    board = [-1 for _ in range(15)]
    cnt = 0
    n_queen(0)
    return cnt


def n_queen(row):
    global cnt
    if row == N:
        cnt += 1
        return 0
    for col in range(N):
        board[row] = col
        if promising(row):
            n_queen(row + 1)


def promising(row):
    for comp_r in range(row):
        if board[row] == board[comp_r] or (row - comp_r) == abs(board[row] - board[comp_r]):
            return False
    return True


print(solution())
