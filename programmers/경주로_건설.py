# 위, 오른쪽, 아래, 왼쪽
# 0, 1, 2, 3
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
N = 0
STRAIGHT = 0
CORNER = 1

land = []
visited = []


def solution(board):
    global N, land, visited
    N = len(board)
    land = board
    visited = [[float('inf') for _ in range(N)] for _ in range(N)]
    visited[0][0] = 0
    dfs(0, 0, -1, [0, 0])
    return visited[-1][-1]


def dfs(r, c, prev_dir, road_type_to_num):
    global visited
    for dir in range(4):
        nr, nc = r + dr[dir], c + dc[dir]
        road_type_to_num[get_road_type(prev_dir, dir)] += 1
        cost = cal_cost(road_type_to_num)
        if is_in(nr, nc) and cost <= visited[nr][nc] and not land[nr][nc]:
            visited[nr][nc] = cost
            dfs(nr, nc, dir, road_type_to_num)
        road_type_to_num[get_road_type(prev_dir, dir)] -= 1


def is_in(r, c):
    return 0 <= r < N and 0 <= c < N


def get_road_type(prev_dir, cur_dir):
    if prev_dir == -1 or prev_dir == cur_dir:
        return STRAIGHT
    else:
        return CORNER


def cal_cost(road_type_to_num: dict):
    return road_type_to_num[STRAIGHT] * 100 + road_type_to_num[CORNER] * 600


if __name__ == "__main__":
    # print(solution([[0,0,0],[0,0,0],[0,0,0]]))
    # print(solution(
    #     [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
    #      [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]))
    print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
