from collections import deque

L, R, U, D = (0, -1), (0, 1), (-1, 0), (1, 0)


def solution():
    N = int(input())
    K = int(input())
    apple_coords = {}
    for _ in range(K):
        coord = tuple(map(int, input().split(" ")))
        apple_coords[coord] = True
    L = int(input())
    dir_change_info = {}
    for _ in range(L):
        tmp = input().split(" ")
        dir_change_info[int(tmp[0])] = tmp[1]
    sec = 0
    snake_body = deque([(1, 1)])
    snake_head = (1, 1)
    snake_dir = R
    while True:
        sec += 1
        snake_head = move(snake_head, snake_dir)
        if check_game_over(snake_head, snake_body, N):
            return sec
        snake_body.append(snake_head)
        if snake_head not in apple_coords:
            snake_body.popleft()
        if sec in dir_change_info:
            snake_dir = change_dir(snake_dir, dir_change_info[sec])


def move(snake_head, snake_dir):
    h_row, h_col = snake_head
    return (h_row + snake_dir[0], h_col + snake_dir[1])


def check_game_over(head, body, N):
    if head in body:
        return True
    h_row, h_col = head
    if h_row == 0 or h_row == N + 1 or h_col == 0 or h_col == N + 1:
        return True
    return False


def change_dir(snake_dir, rotate_dir):
    dirs = [R, D, L, U]
    dir_idx = dirs.index(snake_dir)
    if rotate_dir == "D":  # 오른쪽
        return dirs[(dir_idx + 1) % 4]
    else:
        return dirs[(dir_idx - 1) % 4]


print(solution())
