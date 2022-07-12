board = []
visited = []
coords = []
NUM_REC = 0;

dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]

def solution(rectangle, characterX, characterY, itemX, itemY):
    global board, visited, coords, NUM_REC
    answer = 0
    coords = [set() for _ in range(len(rectangle))]
    board = [[0 for _ in range(51)] for _ in range(51)]
    visited = [[0 for _ in range(51)] for _ in range(51)]
    NUM_REC = len(rectangle)
    for i, rec in enumerate(rectangle):
        l_u_x, l_u_y, r_d_x, r_d_y = rec
        for x in range(l_u_x, r_d_x + 1):
            for y in [l_u_y, r_d_y]:
                board[x][y] = 1
                coords[i].add((x, y))
        for y in range(l_u_y, r_d_y):
            for x in [l_u_x, r_d_x]:
                board[x][y] = 1
                coords[i].add((x, y))

    return answer


def dfs(x, y, cur_rec_i):
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if is_in(nx, ny) and not visited[nx][ny] and


def is_in(x, y):
    return 0 <= x <= 50 and 0 <= y <= 50


print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))