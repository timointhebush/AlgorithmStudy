from collections import defaultdict, deque
from itertools import permutations, product
import copy


def solution(board, r, c):
    answer = float('inf')
    card_to_coords_1 = defaultdict(list)
    card_to_coords_2 = defaultdict(list)
    cards = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 0:
                card = board[i][j]
                cards.add(card)
                card_to_coords_1[card].append((i, j))
    for card, coords in card_to_coords_1.items():
        coords_2 = [coords[1], coords[0]]
        card_to_coords_2[card] = coords_2

    cards = list(cards)
    card_cases = permutations(cards, len(cards))
    cache = {}
    for card_case in card_cases:
        final_cases = create_final_case(card_case, card_to_coords_1, card_to_coords_2)
        for final_case in final_cases:
            # print("case: ", final_case)
            cur = (r, c)
            case_moves = 0
            c_board = copy.deepcopy(board)
            for i, nxt in enumerate(final_case):
                move = get_min_move(cur, nxt, c_board, cache)
                # print(cur, " to ", nxt)
                # print("move: ", move)
                case_moves += move
                if (i + 1) % 2 == 0:
                    c_board[cur[0]][cur[1]] = 0
                    c_board[nxt[0]][nxt[1]] = 0
                cur = nxt
            # if case_moves == 9:
            #     print("----------------------")
            if case_moves < answer:
                answer = case_moves
    return answer + (2 * len(cards))


def create_final_case(card_case, coords_1, coords_2):
    num_to_coords = {0: coords_1, 1: coords_2}
    num_cases = product(range(2), repeat=len(card_case))
    final_cases = []
    for case in num_cases:
        final_case = []
        for i in range(len(case)):
            card = card_case[i]
            coords = num_to_coords[case[i]]
            final_case.extend(coords[card])
        final_cases.append(final_case)
    return final_cases


def get_min_move(cur, nxt, board, cache):
    if cur == nxt:
        return 0

    depth = 0
    q = deque([(cur[0], cur[1], depth)])
    visited = {cur}
    while q:
        r, c, depth = q.popleft()
        cases = _get_all_move_cases((r, c), board)
        for cr, cc in cases:
            if (cr, cc) == nxt:
                return depth + 1
            if (0 <= cr <= 3 and 0 <= cc <= 3) and (cr, cc) not in visited:
                visited.add((cr, cc))
                q.append((cr, cc, depth + 1))


def _get_all_move_cases(coords, board):
    r, c = coords
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    one_move = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
    ctrl_move = []
    for dr, dc in delta:
        k = 1
        while True:
            nr, nc = r + dr*k, c + dc*k
            if nr < 0 or nr > 3 or nc < 0 or nc > 3:
                ctrl_move.append((nr - dr, nc - dc))
                break
            if board[nr][nc] != 0:
                ctrl_move.append((nr, nc))
                break
            k += 1

    cases = one_move + ctrl_move
    return list(set(cases))

import time
start = time.time()
print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))
print(time.time() - start)