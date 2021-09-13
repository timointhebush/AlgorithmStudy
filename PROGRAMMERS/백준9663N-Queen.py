def solution():
    global board, N
    N = int(input())
    board = [-1 for _ in range(15)]
    cnt = 0
    n_queen(0, 0)
    return cnt


def n_queen(row, cnt):
    if row == N:
        cnt += 1
        print(cnt)
    else:
        for col in range(N):
            board[row] = col
            if promising(row):
                n_queen(row + 1, cnt)


def promising(row):
    for comp_r in range(row - 1):
        if board[row] == board[comp_r] or (row - comp_r) == abs(board[row] - board[comp_r]):
            return False
    return True


print(solution())
