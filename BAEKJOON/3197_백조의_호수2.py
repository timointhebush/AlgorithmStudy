from collections import deque
import sys


def is_connected():
    while q:
        x, y = q.popleft()
        if x == x2 and y == y2:
            return 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if not c[nx][ny]:
                    if lake[nx][ny] == ".":
                        q.append([nx, ny])
                    else:
                        q_temp.append([nx, ny])
                    c[nx][ny] = 1
    return 0


def melt():
    while wq:
        x, y = wq.popleft()
        if lake[x][y] == "X":
            lake[x][y] = "."
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if not wc[nx][ny]:
                    if lake[nx][ny] == "X":
                        wq_temp.append([nx, ny])
                    else:
                        wq.append([nx, ny])
                    wc[nx][ny] = 1


input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

R, C = map(int, input().split())
c = [[0] * C for _ in range(R)]
wc = [[0] * C for _ in range(R)]

lake, swan = [], []
q, q_temp, wq, wq_temp = deque(), deque(), deque(), deque()

for i in range(R):
    row = list(input().strip())
    lake.append(row)
    for j, k in enumerate(row):
        if lake[i][j] == "L":
            swan.extend([i, j])
            wq.append([i, j])
        elif lake[i][j] == ".":
            wc[i][j] = 1
            wq.append([i, j])

x1, y1, x2, y2 = swan
q.append([x1, y1])
lake[x1][y1], lake[x2][y2], c[x1][y1] = ".", ".", 1
cnt = 0

while True:
    melt()
    if is_connected():
        print(cnt)
        break
    q, wq = q_temp, wq_temp
    q_temp, wq_temp = deque(), deque()
    cnt += 1
