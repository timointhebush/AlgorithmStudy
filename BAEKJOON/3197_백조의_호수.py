from collections import deque


def solution(R, C, lake, swans):
    day = 0
    melted = deque()
    while True:
        if is_swan_connected(lake, swans):
            print(day)
            return 0
        melted = melt(R, C, lake, melted)
        day += 1


def is_swan_connected(lake, swans):
    visited = set([swans[0]])
    queue = deque([swans[0]])
    while queue:
        sr, sc = queue.popleft()
        connected = [(sr - 1, sc), (sr + 1, sc), (sr, sc - 1), (sr, sc + 1)]
        for cr, cc in connected:
            if (cr, cc) == swans[1]:
                return True
            if (cr, cc) not in visited and lake[cr][cc] != "W":
                visited.add((cr, cc))
                if lake[cr][cc] != "X":
                    queue.append((cr, cc))
    return False


def melt(R, C, lake, melted):
    visited = set()
    if len(melted) == 0:
        for r in range(1, 1 + R):
            for c in range(1, 1 + C):
                if (r, c) not in visited and lake[r][c] == ".":
                    visited.add((r, c))
                    queue = deque([(r, c)])
                    while queue:
                        sr, sc = queue.popleft()
                        connected = [(sr - 1, sc), (sr + 1, sc), (sr, sc - 1), (sr, sc + 1)]
                        for cr, cc in connected:
                            if (cr, cc) not in visited and lake[cr][cc] != "W":
                                visited.add((cr, cc))
                                if lake[cr][cc] == "X":
                                    lake[cr][cc] = "."
                                    melted.append((cr, cc))
                                else:
                                    queue.append((cr, cc))
        return melted
    else:
        new_melted = deque()
        while melted:
            sr, sc = melted.popleft()
            connected = [(sr - 1, sc), (sr + 1, sc), (sr, sc - 1), (sr, sc + 1)]
            for cr, cc in connected:
                if (cr, cc) not in visited and lake[cr][cc] != "W":
                    visited.add((cr, cc))
                    if lake[cr][cc] == "X":
                        lake[cr][cc] = "."
                        new_melted.append((cr, cc))
        return new_melted


if __name__ == "__main__":
    R, C = tuple(map(int, input().split(" ")))
    lake = [["W" for _ in range(C + 2)] for _ in range(R + 2)]
    swans = []
    for r in range(1, 1 + R):
        row = list(input())
        for c in range(1, 1 + C):
            lake[r][c] = row[c - 1]
            if row[c - 1] == "L":
                swans.append((r, c))
    solution(R, C, lake, swans)
