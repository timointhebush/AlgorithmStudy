from collections import deque


def solution():
    global N, M, map_
    N, M = tuple(map(int, input().split(" ")))
    map_ = []
    land_coords = []
    for row in range(N):
        line = list(map(int, input().split(" ")))
        for col, num in enumerate(line):
            if num == 1:
                land_coords.append((row, col))
        map_.append(line)
    num_coords, coords_num = identify_island(land_coords)
    nums_bridge_lens = get_nums_bridge_lens(num_coords, coords_num)
    # print(num_coords)
    # print(nums_bridge_lens)
    del_duplicate_nums(nums_bridge_lens)
    if len(nums_bridge_lens) == 0:
        return -1
    # leave_shortest_len(nums_bridge_lens)
    graph = make_graph(nums_bridge_lens)
    if len(graph) != len(num_coords):
        return -1
    # print(graph)
    return mst(graph)


def mst(graph):
    dist = {i: float("inf") for i in range(1, len(graph) + 1)}
    V = set(range(1, len(graph) + 1))
    S = set()
    dist[1] = 0
    while S != V:
        node = extract_min(V - S, dist)
        S.add(node)
        for connected in graph[node]:
            if connected[0] in V - S and connected[1] < dist.get(connected[0]):
                dist[connected[0]] = connected[1]
    # print(dist)
    bridge_len = sum(dist.values())

    return -1 if bridge_len == 0 else bridge_len


def extract_min(not_visited, dist):
    min_i = list(not_visited)[0]
    min_dist = dist[min_i]
    for i in list(not_visited):
        if dist.get(i) < min_dist:
            min_dist = dist.get(i)
            min_i = i
    return min_i


def make_graph(nums_bridge_lens):
    graph = {}
    for nums, lens in nums_bridge_lens.items():
        depart, arrive = nums
        if depart in graph:
            graph[depart].append((arrive, min(lens)))
        else:
            graph[depart] = [(arrive, min(lens))]
    return graph


def del_duplicate_nums(nums_bridge_lens):
    del_key_list = []
    for depart, arrive in nums_bridge_lens.keys():
        if depart == arrive:
            del_key_list.append((depart, arrive))
    for del_key in del_key_list:
        del nums_bridge_lens[del_key]
    reversed_key_list = []
    # print(nums_bridge_lens)


def get_nums_bridge_lens(num_coords, coords_num):
    nums_bridge_lens = {}
    for land_coord, depart_island_num in coords_num.items():
        around_sea_coords = get_around_sea_coords(land_coord)
        if len(around_sea_coords) != 0:
            for sea_coord in around_sea_coords:
                arrive_island_num, bridge_len = try_build_bridge(land_coord, sea_coord, coords_num)
                if arrive_island_num != 0:
                    add_bridge(nums_bridge_lens, depart_island_num, arrive_island_num, bridge_len)
    return nums_bridge_lens


def try_build_bridge(land_coord, sea_coord, coords_num):
    bridge_len = 1
    dir_row, dir_col = sea_coord[0] - land_coord[0], sea_coord[1] - land_coord[1]
    b_row, b_col = land_coord[0] + dir_row, land_coord[1] + dir_col
    while True:
        n_b_row, n_b_col = b_row + dir_row, b_col + dir_col
        if is_in_map((n_b_row, n_b_col)) == False:
            return 0, bridge_len
        if map_[n_b_row][n_b_col] == 1:
            arrive_island_num = coords_num[(n_b_row, n_b_col)]
            if bridge_len >= 2:
                return arrive_island_num, bridge_len
            else:
                return 0, bridge_len
        b_row, b_col = n_b_row, n_b_col
        bridge_len += 1


def add_bridge(nums_bridge_lens, depart_island_num, arrive_island_num, bridge_len):
    if (depart_island_num, arrive_island_num) in nums_bridge_lens:
        nums_bridge_lens[(depart_island_num, arrive_island_num)].append(bridge_len)
    else:
        nums_bridge_lens[(depart_island_num, arrive_island_num)] = [bridge_len]


def identify_island(land_coords):
    num_coords, coords_num = {}, {}
    visited = set()
    island_num = 1
    while len(visited) != len(land_coords):
        num_coords[island_num] = []
        queue = deque()
        start_coord = list(set(land_coords) - visited)[0]
        queue.append(start_coord)
        visited.add(start_coord)
        num_coords[island_num].append(start_coord)
        coords_num[start_coord] = island_num
        while len(queue) != 0:
            start_land_coord = queue.popleft()
            around_land_coords = get_around_land_coords(start_land_coord)
            for a_l_c in around_land_coords:
                if a_l_c not in visited:
                    queue.append(a_l_c)
                    visited.add(a_l_c)
                    num_coords[island_num].append(a_l_c)
                    coords_num[a_l_c] = island_num
        island_num += 1

    return num_coords, coords_num


def get_around_coords(start_coord):
    row, col = start_coord
    return [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]


def get_around_land_coords(start_coord):
    cand_coords = get_around_coords(start_coord)
    land_coords = []
    for coord in cand_coords:
        if is_in_map(coord) and is_land(coord):
            land_coords.append(coord)
    return land_coords


def get_around_sea_coords(start_coord):
    cand_coords = get_around_coords(start_coord)
    sea_coords = []
    for coord in cand_coords:
        if is_in_map(coord) and is_sea(coord):
            sea_coords.append(coord)
    return sea_coords


def is_in_map(coord):
    row, col = coord
    if row >= 0 and row < N and col >= 0 and col < M:
        return True
    return False


def is_land(coord):
    row, col = coord
    if map_[row][col] == 1:
        return True
    return False


def is_sea(coord):
    row, col = coord
    if map_[row][col] == 0:
        return True
    return False


print(solution())
