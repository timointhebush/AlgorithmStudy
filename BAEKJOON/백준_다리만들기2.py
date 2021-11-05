from collections import deque


def solution():
    global board, N, M
    NM = input().split(" ")
    N, M = int(NM[0]), int(NM[1])
    land_coords = {}
    board = []
    for row in range(N):
        tmp = input().split(" ")
        for col in range(M):
            tmp[col] = int(tmp[col])
            if tmp[col] == 1:
                land_coords[(row, col)] = None
        board.append(tmp)
    # for _ in board:
    #     print(_)
    # print(land_coords)
    island_num_coords = {}
    visited = set()
    num = 0
    while len(visited) < len(land_coords):
        queue = deque()
        queue.append(get_not_visited(land_coords))
        while len(queue) != 0:
            start = queue.popleft()
            around = get_around(start)
            for coord in around:
                if coord not in visited and coord in land_coords:
                    # print(coord)
                    visited.add(coord)
                    queue.append(coord)
                    land_coords[coord] = num
        num += 1
        # print(land_coords)
    # print(land_coords)
    for coord in land_coords.keys():
        around = get_around(coord)
        for a_coord in around:
            row, col = a_coord
            if check_in_board(row, col) and board[row][col] == 0:
                bridges = build_bridge(coord, a_coord)


def get_not_visited(land_coords):
    for coord in land_coords.keys():
        if land_coords[coord] == None:
            return coord


def get_around(coord):
    row, col = coord
    return [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]


def check_in_board(row, col):
    if row >= 0 and row < N and col >= 0 and col < M:
        return True
    else:
        return False


print(solution())
