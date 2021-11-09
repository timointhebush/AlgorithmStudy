import copy


def solution():
    board = [[0 for _ in range(4)] for _ in range(4)]
    dict_fish_coord = {}
    for row in range(4):
        tmp = list(map(int, input().split(" ")))
        for col in range(4):
            board[row][col] = (tmp[col * 2], tmp[col * 2 + 1])
            dict_fish_coord[tmp[col * 2]] = (row, col)
    for _ in board:
        print(_)
    print(dict_fish_coord)
    # 첫 상어 입장, 상어는 0번
    first_eaten = board[0][0][0]
    first_dir = board[0][0][1]
    del dict_fish_coord[first_eaten]
    dict_fish_coord[0] = (0, 0)
    board[0][0] = (0, first_dir)
    move_fishes(board, dict_fish_coord)
    for _ in board:
        print(_)

    shark_move_cand = get_shark_move_cand(board, dict_fish_coord)
    print(shark_move_cand)
    eaten_nums = []
    for move_cand in shark_move_cand:
        copy_board = copy.deepcopy(board)
        copy_dict_fish_coord = copy.deepcopy(dict_fish_coord)
        eaten_nums.append(get_eaten_num(copy_board, move_cand, first_eaten, copy_dict_fish_coord))
        print("case", move_cand)
        for _ in copy_board:
            print(_)
        print(eaten_nums)
    # return max(eaten_nums)


def dfs(board, move_cand, eaten_num, dict_fish_coord):
    eaten_num = get_eaten_num(board, move_cand, eaten_num, dict_fish_coord)
    move_fishes(board, dict_fish_coord)
    shark_move_cand = get_shark_move_cand(board, dict_fish_coord)
    if len(shark_move_cand) != 0:
        for s_move_cand in shark_move_cand:
            return dfs(board, s_move_cand, eaten_num, dict_fish_coord)
    else:
        return eaten_num


def get_eaten_num(board, move_cand, eaten_num, dict_fish_coord):
    eaten_fish = board[move_cand[0]][move_cand[1]]
    del dict_fish_coord[eaten_fish[0]]
    eaten_num += eaten_fish[0]

    s_row, s_col = dict_fish_coord[0]
    shark = board[s_row][s_col]
    board[move_cand[0]][move_cand[1]] = (0, eaten_fish[1])
    board[s_row][s_col] = None
    dict_fish_coord[0] = (move_cand[0], move_cand[1])

    return eaten_num


def get_shark_move_cand(board, dict_fish_coord):
    s_row, s_col = dict_fish_coord[0]
    s_dir = board[s_row][s_col][1]

    move_cand = []
    while True:
        n_row, n_col = get_dir_coord(s_row, s_col, s_dir)
        if is_out(n_row, n_col) == False:
            move_cand.append((n_row, n_col))
            s_row, s_col = n_row, n_col
            n_row, n_col = get_dir_coord(s_row, s_col, s_dir)
        else:
            return move_cand


def move_fishes(board, dict_fish_coord):
    for fish_num in range(1, 17):
        if fish_num in dict_fish_coord:
            fish_coord = dict_fish_coord[fish_num]
            move_the_fish(board, fish_coord, dict_fish_coord)
            print(fish_num)
            for _ in board:
                print(_)


def move_the_fish(board, fish_coord, dict_fish_coord):
    row, col = fish_coord
    fish_num = board[row][col][0]
    fish_dir = board[row][col][1]

    for _ in range(8):
        n_row, n_col = get_dir_coord(row, col, fish_dir)
        if is_out(n_row, n_col) or is_shark(board, n_row, n_col):
            fish_dir = (fish_dir % 8) + 1  # 회전
        elif board[n_row][n_col] == None:  # 빈칸
            board[n_row][n_col] = (fish_num, fish_dir)
            dict_fish_coord[fish_num] = (n_row, n_col)
            break
        else:  # 다른 물고기
            tmp_fish = board[n_row][n_col]
            board[n_row][n_col] = (fish_num, fish_dir)
            board[row][col] = tmp_fish
            dict_fish_coord[fish_num] = (n_row, n_col)
            dict_fish_coord[tmp_fish[0]] = (row, col)
            break


def get_dir_coord(row, col, fish_dir):
    diff = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
    d_row, d_col = diff[fish_dir - 1]
    return row + d_row, col + d_col


def is_out(n_row, n_col):
    if n_row >= 0 and n_row < 4 and n_col >= 0 and n_col < 4:
        return False
    return True


def is_shark(board, n_row, n_col):
    if board[n_row][n_col][0] == 0:
        return True
    return False


print(solution())
