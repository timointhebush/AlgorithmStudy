import sys
import copy

input = sys.stdin.readline

def cal(board, target_r, target_c, merged, direction):
    dr, dc = direction_to_delta[direction]
    pointer_r, pointer_c = target_r, target_c
    is_num = False
    while True:
        n_pointer_r, n_pointer_c = pointer_r + dr, pointer_c + dc
        if board[n_pointer_r][n_pointer_c] == -1:
            break
        if board[n_pointer_r][n_pointer_c] != 0:
            is_num = True
            break
        pointer_r, pointer_c = n_pointer_r, n_pointer_c
    if is_num and board[n_pointer_r][n_pointer_c] == board[target_r][target_c] \
            and merged[n_pointer_r][n_pointer_c] == False:
        tmp = board[target_r][target_c]
        board[target_r][target_c] = 0
        board[n_pointer_r][n_pointer_c] += tmp
        merged[n_pointer_r][n_pointer_c] = True
    else:
        tmp = board[target_r][target_c]
        board[target_r][target_c] = 0
        board[pointer_r][pointer_c] = tmp

def up(board, merged):
    for target_r in range(1, N + 1):
        for target_c in range(1, N + 1):
            cal(board, target_r, target_c, merged, 'U')

def down(board, merged):
    for target_r in range(N, 0, -1):
        for target_c in range(N, 0, -1):
            cal(board, target_r, target_c, merged, 'D')

def right(board, merged):
    for target_c in range(N, 0, -1):
        for target_r in range(1, N + 1):
            cal(board, target_r, target_c, merged, 'R')

def left(board, merged):
    for target_c in range(1, N + 1):
        for target_r in range(N, 0, -1):
            cal(board, target_r, target_c, merged, 'L')

def swipe(direction, board):
    merged = [[False for _ in range(N + 2)] for _ in range(N + 2)]
    if direction == 'U':
        up(board, merged)
    elif direction == 'R':
        right(board, merged)
    elif direction == 'D':
        down(board, merged)
    else: # L
        left(board, merged)
    return board

def get_max_val(board):
    max_val_list = [max(_) for _ in board]
    return max(max_val_list)

def dfs(board, depth):
    if depth == 5:
        # for _ in board:
        #     print(_)
        # print()
        return get_max_val(board)
    max_val_list = []
    for direction in ["U", "R", "D", "L"]:
        swiped_board = swipe(direction, copy.deepcopy(board))
        max_val_list.append(dfs(swiped_board, depth + 1))
    return max(max_val_list)

if __name__ == '__main__':
    N = int(input())
    board = [[-1 for _ in range(N + 2)] for _ in range(N + 2)]
    direction_to_delta = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}
    for n in range(N):
        row = list(map(int, input().split()))
        for m in range(N):
            board[n + 1][m + 1] = row[m]
    print(dfs(board, 0))