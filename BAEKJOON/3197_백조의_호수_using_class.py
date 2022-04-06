from collections import deque
import sys


class Solution:
    def __init__(self, lake, swan_visited, melt_visited, swan_q, melt_q, swans) -> None:
        self.lake = lake
        self.swan_visited = swan_visited
        self.melt_visited = melt_visited
        self.swan_q = swan_q
        self.melt_q = melt_q
        self.swan_q_tmp, self.melt_q_tmp = deque(), deque()
        self.target_swan = swans[1]
        self.swan_q.append(swans[0])
        self.swan_visited.add(swans[0])

    def is_swan_connected(self):
        while self.swan_q:
            r, c = self.swan_q.popleft()
            if (r, c) == self.target_swan:
                return True
            connected = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for cr, cc in connected:
                if self.lake[cr][cc] != "W" and (cr, cc) not in self.swan_visited:
                    self.swan_visited.add((cr, cc))
                    if self.lake[cr][cc] != "X":
                        self.swan_q.append((cr, cc))
                    else:  # == 'X'
                        self.swan_q_tmp.append((cr, cc))
        return False

    def melt(self):
        while self.melt_q:
            r, c = self.melt_q.popleft()
            if self.lake[r][c] == "X":
                self.lake[r][c] = "."
            connected = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for cr, cc in connected:
                if self.lake[cr][cc] != "W" and (cr, cc) not in self.melt_visited:
                    self.melt_visited.add((cr, cc))
                    if self.lake[cr][cc] == "X":
                        self.melt_q_tmp.append((cr, cc))
                    else:
                        self.melt_q.append((cr, cc))

    def switch(self):
        self.swan_q, self.melt_q = self.swan_q_tmp, self.melt_q_tmp
        self.swan_q_tmp, self.melt_q_tmp = deque(), deque()


if __name__ == "__main__":
    R, C = tuple(map(int, sys.stdin.readline().split()))
    swan_visited, melt_visited = set(), set()
    swan_q = deque()
    melt_q = deque()

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
    sol = Solution(lake, swan_visited, melt_visited, swan_q, melt_q, swans)

    day = 0
    while True:
        sol.melt()
        if sol.is_swan_connected():
            print(day)
            break
        sol.switch()
        day += 1
