import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while q:
        red_r, red_c, blue_r, blue_c, depth = q.popleft()
        if depth >= 10: 
            return -1
        for direction in dir_list:
            n_red_r, n_red_c, red_cnt, red_stop_type = lean(red_r, red_c, direction)
            n_blue_r, n_blue_c, blue_cnt, blue_stop_type = lean(blue_r, blue_c, direction)
            if blue_stop_type == 'hole':
                continue
            if red_stop_type == 'hole':
                return depth + 1

            if n_red_c == n_blue_c and n_red_r == n_blue_r:
                dr, dc = dir_to_coord[direction]
                if red_cnt > blue_cnt:
                    n_red_r, n_red_c = n_red_r - dr, n_red_c - dc
                else:
                    n_blue_r, n_blue_c = n_blue_r - dr, n_blue_c - dc
            
            if (n_red_r, n_red_c, n_blue_r, n_blue_c) not in visited:
                visited.add((n_red_r, n_red_c, n_blue_r, n_blue_c))
                q.append((n_red_r, n_red_c, n_blue_r, n_blue_c, depth + 1))
    return -1


def lean(row, col, direction):
    dr, dc = dir_to_coord[direction]
    n_row, n_col = row + dr, col + dc
    move_cnt = 0
    while True:
        if board[n_row][n_col] == '#':
            return row, col, move_cnt, 'wall'
        elif board[n_row][n_col] == 'O':
            return row, col, move_cnt, 'hole'
        row, col = n_row, n_col
        n_row, n_col = row + dr, col + dc
        move_cnt += 1



if __name__ == '__main__':
    N, M = tuple(map(int, input().split()))
    board = []
    red_r, red_c, blue_r, blue_c = 0, 0, 0, 0
    hole = (0, 0)
    depth = 0
    # 보드 생성, 각 좌표 확인
    for n in range(N):
        row = list(input())
        board.append(row)
        for m in range(M):
            if row[m] == 'R':
                red_r, red_c = n, m
            elif row[m] == 'B':
                blue_r, blue_c = n, m
            elif row[m] == 'O':
                hole = (n, m)
    
    dir_list = ['U', 'R', 'D', 'L']
    dir_to_coord = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}

    q = deque([(red_r, red_c, blue_r, blue_c, depth)])
    visited = set([(red_r, red_c, blue_r, blue_c)])

    print(bfs())