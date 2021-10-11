def solution(N):
    processor = [[0 for _ in range(N)] for _ in range(N)]
    core_coords = []
    for row_i in range(N):
        row = input().split(" ")
        for col_i in range(N):
            if row[col_i] == "1":
                processor[row_i][col_i] = 1
                core_coords.append((row_i, col_i))
    already_connected_num = 0
    coord_moving_cand = {}
    for coord in core_coords:
        if coord[0] == 0 or coord[0] == N-1 or coord[1] == 0 or coord[1] == N-1:
            already_connected_num +=1
        else:
            coord_moving_cand[coord] = get_coord_moving_cand() # 아무 연결하지 않은 경우도 포함해야함.
    not_edge_cores_coord = list(coord_moving_cand.keys())
    connected_history = [-1 for _ in range(len())]
    dfs(0, connected_history, coord_moving_cand)
    print(core_coords)

def dfs(depth, connected_history, coord_moving_cand):
    if depth == len(connected_history):
        # 코어 갯수와 길이 후보군에 추가함.
    

test_cases = int(input())
for _ in range(test_cases):
    N = int(input())
    solution(N)
