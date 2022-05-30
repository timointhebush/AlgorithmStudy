from collections import deque
from itertools import permutations, product


def solution(board, r, c):
    global min_cost, cards_coord, new_board
    new_board = [[7 for _ in range(n + 2)] for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    cards_coord = {"start": (r, c)}
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] != 0:
                card = board[row][col]
                if card not in cards_coord:
                    cards_coord[card] = [(row, col)]
                else:
                    cards_coord[card].append((row, col))
    # min_cost[i][j] = i에서 j로 이동하고, j와 같은 카드까지 제거하는 데 드는 최소비용
    min_cost = [[-1 for _ in range(len(board) * 2 + 1)] for _ in range(len(board) * 2 + 1)]
    card_cases = permutations(range(1, len(cards_coord) + 1))
    costs = []
    for case in card_cases:
        order_cases = product(
            (0,),
            (case[0] * 2 - 1, case[0] * 2),
            (case[1] * 2 - 1, case[1] * 2),
            (case[2] * 2 - 1, case[2] * 2),
        )
        for order_case in order_cases:
            cost = 0
            for i in range(len(order_case) - 1):
                cost += get_min_cost(order_case[i], order_case[i + 1])
            costs.append(cost)
    return min(costs)


def get_min_cost(a, b):
    if min_cost[a][b] != -1:
        return min_cost[a][b]
    if a == 0:
        sr, sc = cards_coord["start"]
        er, ec = cards_coord[(b + (b % 2)) / 2][b % 2]

def cal_min_cost(sr, sc, er, ec, board):
    


def get_next_moves(r, c, new_board):
    next_moves = set()
    if new_board[r][c] != 0:
        next_moves.add((r, c))
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r + dr, c + dc
        if new_board[nr][nc] != 7:
            next_moves.add((nr, nc))

    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r + dr, c + dc
        while new_board[nr][nc] not in [1, 2, 3, 4, 5, 6]:
            if new_board[nr][nc] == 7:
                nr, nc = nr - dr, nc - dc
                break
            else:
                nr, nc = nr + dr, nc + dc
        next_moves.add((nr, nc))
    return next_moves


print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0))
