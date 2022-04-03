from collections import deque
import sys


class Solution:
    def __init__(self, lake, swans, lands):
        self.lake = lake
        self.swans = swans
        self.target_swan = swans[1]
        self.lands = lands

        self.melt_q, self.swan_q = deque(), deque()
        self.melt_q_tmp, self.swan_q_tmp = deque(), deque()
        self.melt_visited, self.swan_visited = set(), set()

        self.melt_q.extend(lands)
        self.melt_q.extend(swans)

        self.swan_q.append(swans[0])
        self.lake[swans[0][0]][swans[0][1]] = "."
        self.lake[swans[1][0]][swans[1][1]] = "."

    def melt(self):
        while self.melt_q:
            r, c = self.melt_q.popleft()
            if self.lake[r][c] == "X":
                self.lake[r][c] = "."

            connected = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for cr, cc in connected:
                if (cr, cc) not in self.melt_visited and self.lake[cr][cc] != "W":
                    self.melt_visited.add((cr, cc))
                    if self.lake[cr][cc] == "X":
                        self.melt_q_tmp.append((cr, cc))
                    else:
                        self.melt_q.append((cr, cc))

    def is_swan_connected(self):
        while self.swan_q:
            r, c = self.swan_q.popleft()
            if (r, c) == self.target_swan:
                return True

            connected = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for cr, cc in connected:
                if (cr, cc) not in self.swan_visited and self.lake[cr][cc] != "W":
                    self.swan_visited.add((cr, cc))
                    if self.lake[cr][cc] == ".":
                        self.swan_q.append((cr, cc))
                    else:
                        self.swan_q_tmp.append((cr, cc))
        return False

    def swap_q(self):
        self.melt_q, self.swan_q = self.melt_q_tmp, self.swan_q_tmp
        self.melt_q_tmp, self.swan_q_tmp = deque(), deque()


if __name__ == "__main__":
    input = sys.stdin.readline
    R, C = tuple(map(int, input().split(" ")))
    lake = [["W" for _ in range(C + 2)] for _ in range(R + 2)]
    swans = []
    lands = set()
    for r in range(1, 1 + R):
        row = list(input())
        for c in range(1, 1 + C):
            lake[r][c] = row[c - 1]
            if row[c - 1] == "L":
                swans.append((r, c))
            if row[c - 1] == ".":
                lands.add((r, c))
    sol = Solution(lake, swans, lands)
    day = 0
    while True:
        sol.melt()
        if sol.is_swan_connected():
            print(day)
            break
        sol.swap_q()
        day += 1
