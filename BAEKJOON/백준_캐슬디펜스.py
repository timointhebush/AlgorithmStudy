from itertools import combinations


def solution():
    tmp = input().split(" ")
    global N, D
    N, M, D = int(tmp[0]), int(tmp[1]), int(tmp[2])
    enemies_coord = []
    for row_i in range(N):
        row = input().split(" ")
        for col_i in range(M):
            if row[col_i] == "1":
                enemies_coord.append((row_i, col_i))
    ans_cand = []
    for case in combinations(range(M), 3):
        archers_coord = [(N, case[0]), (N, case[1]), (N, case[2])]
        copy_enemies_coord = enemies_coord[:]
        play_game(copy_enemies_coord, archers_coord, ans_cand)
    print(max(ans_cand))


def play_game(enemies_coord, archers_coord, ans_cand):
    kill = 0

    while len(enemies_coord) != 0:

        target_enemy = set()
        for archer in archers_coord:
            min_dis = float("inf")
            min_enemy = []
            for enemy in enemies_coord:
                if distance(archer, enemy) <= D:
                    if distance(archer, enemy) == min_dis:
                        min_enemy.append(enemy)
                    elif distance(archer, enemy) < min_dis:
                        min_enemy = []
                        min_dis = distance(archer, enemy)
                        min_enemy.append(enemy)
            if len(min_enemy) >= 2:
                target_enemy.add(get_left_enemy(min_enemy))
            elif len(min_enemy) == 1:
                target_enemy.add(min_enemy[0])

        if len(target_enemy) > 0:
            kill += len(target_enemy)
            for enemy in list(target_enemy):
                enemies_coord.remove(enemy)

        move_enemies(enemies_coord)

    ans_cand.append(kill)


def distance(archer, enemy):
    r1, c1 = archer
    r2, c2 = enemy
    return abs(r1 - r2) + abs(c1 - c2)


def get_left_enemy(min_enemy):
    min_col_coord = float("inf")
    enemy = min_enemy[0]
    for e_r, e_c in min_enemy:
        if e_c < min_col_coord:
            min_col_coord = e_c
            enemy = (e_r, e_c)
    return enemy


def move_enemies(enemies_coord):
    del_list = []
    for i in range(len(enemies_coord)):
        if enemies_coord[i][0] + 1 >= N:
            del_list.append(i)
        else:
            enemies_coord[i] = (enemies_coord[i][0] + 1, enemies_coord[i][1])
    if len(del_list) >= 1:
        for i in range(len(del_list) - 1, -1, -1):
            del enemies_coord[del_list[i]]


solution()
