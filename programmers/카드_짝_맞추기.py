import copy
from itertools import permutations, combinations, product
from collections import defaultdict, deque

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

cache = {}


def solution(board, r, c):
    answer = float('inf')
    card_to_coords = defaultdict(list)
    for nr in range(4):
        for nc in range(4):
            if board[nr][nc] != 0:
                card_to_coords[board[nr][nc]].append((nr, nc))

    for key in card_to_coords.keys():
        tmp = card_to_coords[key]
        tmp_2 = [tmp[1], tmp[0]]
        card_to_coords[key] = [tmp, tmp_2]

    card_num = len(card_to_coords.keys())
    type_cases = list(product(range(2), repeat=card_num))
    card_cases = list(permutations(list(card_to_coords.keys()), card_num))

    for card_case in card_cases:
        for type_case in type_cases:
            card_seq = [(r, c)]
            for i in range(card_num):
                card, type = card_case[i], type_case[i]
                card_seq.extend(card_to_coords[card][type])

            deleted = set()
            tmp_answer = 0
            copy_board = copy.deepcopy(board)
            tmp_answer += (get_min(copy_board, card_seq[0], card_seq[1], deleted) + 1)
            for i in range(1, len(card_seq) - 1):
                a, b = card_seq[i], card_seq[i + 1]
                move = get_min(copy_board, a, b, deleted)
                tmp_answer += move
                tmp_answer += 1
                if i % 2 != 0:
                    copy_board[a[0]][a[1]] = 0
                    copy_board[b[0]][b[1]] = 0
                    deleted.add(a)
                    deleted.add(b)
                if tmp_answer > answer:
                    break
            answer = min(answer, tmp_answer)
    return answer


def get_min(board, a, b, deleted):
    if a == b:
        return 0

    tmp_key = sorted(list(deleted))
    tmp_key.extend([a, b])
    key = tuple(tmp_key)
    if key in cache:
        return cache[key]

    q = deque([(a[0], a[1], 0)])
    visited = set()
    while q:
        r, c, num = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < 4 and 0 <= nc < 4 and (nr, nc):
                if (nr, nc) == b:
                    cache[key] = num + 1
                    return num + 1
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc, num + 1))
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            is_card = False
            while 0 <= nr < 4 and 0 <= nc < 4:
                if (nr, nc) == b:
                    cache[key] = num + 1
                    return num + 1
                if board[nr][nc] != 0:
                    q.append((nr, nc, num + 1))
                    is_card = True
                    break
                nr, nc = nr + dr[i], nc + dc[i]
            if not is_card:
                q.append((nr - dr[i], nc - dc[i], num + 1))


if __name__ == "__main__":
    print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))
    print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1))