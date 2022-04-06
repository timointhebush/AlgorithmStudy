from collections import deque
import sys


def is_swan_connected():
    while swan_q:
        r, c = swan_q.popleft()
        if (r, c) == target_swan:
            return True
        connected = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        for cr, cc in connected:
            if lake[cr][cc] != "W" and (cr, cc) not in swan_visited:
                swan_visited.add((cr, cc))
                if lake[cr][cc] != "X":
                    swan_q.append((cr, cc))
                else:  # == 'X'
                    swan_q_tmp.append((cr, cc))
    return False


def melt():
    while melt_q:
        r, c = melt_q.popleft()
        if lake[r][c] == "X":
            lake[r][c] = "."
        connected = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        for cr, cc in connected:
            if lake[cr][cc] != "W" and (cr, cc) not in melt_visited:
                melt_visited.add((cr, cc))
                if lake[cr][cc] == "X":
                    melt_q_tmp.append((cr, cc))
                else:
                    melt_q.append((cr, cc))


if __name__ == "__main__":
    R, C = tuple(map(int, sys.stdin.readline().split()))
    swan_visited, melt_visited = set(), set()
    swan_q, swan_q_tmp = deque(), deque()
    melt_q, melt_q_tmp = deque(), deque()

    swans = []

    lake = [["W"] * (C + 2) for _ in range(R + 2)]
    for r in range(R):
        row = list(sys.stdin.readline())
        for c in range(C):
            lake[r + 1][c + 1] = row[c]
            if row[c] == "L":
                swans.append((r + 1, c + 1))
                melt_visited.add((r + 1, c + 1))
                melt_q.append((r + 1, c + 1))
            elif row[c] == ".":
                melt_visited.add((r + 1, c + 1))
                melt_q.append((r + 1, c + 1))

    swan_q.append(swans[0])
    swan_visited.add(swans[0])
    target_swan = swans[1]

    day = 0
    while True:
        melt()
        if is_swan_connected():
            print(day)
            break
        swan_q, melt_q = swan_q_tmp, melt_q_tmp
        swan_q_tmp, melt_q_tmp = deque(), deque()
        day += 1
