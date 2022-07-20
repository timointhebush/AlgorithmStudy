import sys
from collections import deque


def solve(hog, house, waters):
    q = deque()



if __name__ == "__main__":
    sys.stdin = open("탈출.txt", "r")

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    hog = (0, 0)
    house = (0, 0)
    waters = []
    board = []

    R, C = tuple(map(int, input()))
    for r in range(R):
        row = list(input())
        for c in range(C):
            if row[c] == "*": # 물
                waters.append((r, c))
            elif row[c] == "D": # 비버 굴
                house = (r, c)
            elif row[c] == "S": # 고슴도치
                hog = (r, c)
        board.append(row)

    print(solve(hog, house, waters))