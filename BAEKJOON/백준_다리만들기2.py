from collections import deque


def solution():
    global N, M
    tmp = input().split(" ")
    N, M = int(tmp[0]), int(tmp[1])
    board = [[0 for _ in range(M)] for _ in range(N)]
    land_coords = []
    for row in range(N):
        tmp_line = input().split(" ")
        for col, num in enumerate(tmp_line):
            if num == "1":
                land_coords.append((row, col))
            board[row][col] = int(tmp_line[col])
    board, max_island_num = sort_island(board, land_coords)
    # for _ in board:
    #     print(_)
    # print("max ", max_island_num)
    bridges = build_bridges(board, land_coords)
    graph = make_graph(bridges)
    # print(graph)
    if set(graph.keys()) != set(range(2, max_island_num + 1)):
        return -1
    return -1 if mst(graph) == float("inf") else mst(graph)


def mst(graph):
    if len(graph) == 0:
        return -1
    islands = set()
    distance = {}
    for island in graph.keys():
        islands.add(island)
        distance[island] = float("inf")
    visited = set()
    distance[list(islands)[0]] = 0
    while visited != islands:
        start_island = get_min_dist(distance, islands - visited)
        visited.add(start_island)
        for connect, length in graph[start_island]:
            if distance[connect] > length and connect not in visited:
                distance[connect] = length
    return sum(list(distance.values()))


def get_min_dist(distance, not_visited):
    min_island = list(not_visited)[0]
    min_dis = distance[min_island]
    for island in list(not_visited):
        if distance[island] < min_dis:
            min_dis = distance[island]
            min_island = island
    return min_island


def make_graph(bridges):
    graph = {}
    for key, lengths in bridges.items():
        depart, arrive = key
        if depart in graph:
            graph[depart].append([arrive, min(lengths)])
        else:
            graph[depart] = [[arrive, min(lengths)]]
    return graph


def build_bridges(board, land_coords):
    bridges = {}
    for coord in land_coords:
        row, col = coord
        around_coords = get_around_sea_coords(coord, board)
        for arow, acol in around_coords:
            arrive_island, length = build(row, col, arow, acol, board)
            if arrive_island != 0:
                depart_island = board[row][col]
                key = (arrive_island, depart_island)
                if key in bridges:
                    bridges[key].append(length)
                else:
                    bridges[key] = [length]
    return bridges


def build(row, col, arow, acol, board):
    crow, ccol = arow - row, acol - col
    length = 0
    brow, bcol = row, col
    while check_outboard(brow, bcol) == False:
        if board[brow][bcol] != board[row][col] and board[brow][bcol] != 0:
            if length < 3:
                return 0, 0
            return board[brow][bcol], length - 1
        length += 1
        brow, bcol = brow + crow, bcol + ccol
    return 0, 0


def sort_island(board, land_coords):
    island_num = 2
    for coord in land_coords:
        row, col = coord
        if board[row][col] == 1:
            # bfs실행하여
            queue = deque([coord])
            visited = [coord]
            board[coord[0]][coord[1]] = island_num
            while len(queue) != 0:
                start_coord = queue.popleft()
                around_coords = get_around_land_coords(start_coord, board)
                for a_coord in around_coords:
                    if a_coord not in visited:
                        queue.append(a_coord)
                        visited.append(a_coord)
                        board[a_coord[0]][a_coord[1]] = island_num
            island_num += 1
    return board, island_num - 1


def get_around_land_coords(coord, board):
    row, col = coord
    cands = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
    around_coords = []
    for r, c in cands:
        if check_outboard(r, c) == False and board[r][c] != 0:
            around_coords.append((r, c))
    return around_coords


def get_around_sea_coords(coord, board):
    row, col = coord
    cands = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
    around_coords = []
    for r, c in cands:
        if check_outboard(r, c) == False and board[r][c] == 0:
            around_coords.append((r, c))
    return around_coords


def check_outboard(row, col):
    if row < 0 or row >= N or col < 0 or col >= M:
        return True
    return False


print(solution())
