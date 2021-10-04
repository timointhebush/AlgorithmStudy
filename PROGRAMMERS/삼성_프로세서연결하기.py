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
    print(core_coords)


test_cases = int(input())
for _ in range(test_cases):
    N = int(input())
    solution(N)
