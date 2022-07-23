import sys
from collections import deque


def solve():
    global board, q
    while q:
        r, c, mi, ty = q.popleft()
        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]
            if (nr, nc) == house and ty == "S":
                return mi + 1
            if board[nr][nc] != "X" and board[nr][nc] != "D" and board[nr][nc] != "S" and board[nr][nc] != "*":
                board[nr][nc] = ty
                q.append((nr, nc, mi + 1, ty))
    return "KAKTUS"


if __name__ == "__main__":
    sys.stdin = open("탈출.txt", "r")

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    hog = (0, 0)
    house = (0, 0)
    waters = []

    R, C = map(int, input().split())
    board = [['X' for _ in range(C + 2)] for _ in range(R + 2)]

    for r in range(R):
        row = list(input())
        for c in range(C):
            val = row[c]
            board[r + 1][c + 1] = val
            if val == "*": # 물
                waters.append((r + 1, c + 1, 0, "*"))
            elif val == "D": # 비버 굴
                house = (r + 1, c + 1)
            elif val == "S": # 고슴도치
                hog = (r + 1, c + 1)

    q = deque(waters)
    q.append((hog[0], hog[1], 0, "S"))

    print(solve())