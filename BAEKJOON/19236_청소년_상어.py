# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

import sys
import copy

'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''

# 잡힌 물고기의 경우 방향이 -1
# fishes에선 None

def print_board(board):
    for _ in board:
        print(_)

def move_fishes(board):
    for fish_num in range(1, 17):
        x, y = -1, -1
        for r in range(4):
            for c in range(4):
                if board[r][c][0] == fish_num:
                    x, y = r, c
                    break
        if x == -1 and y == -1:
            continue

        way = board[x][y][1]
        for i in range(8):
            if i == 0:
                n = 0
            else:
                n = 1
            way = way + n if way + n <= 8 else (way + n) - 8
            board[x][y][1] = way
            dx, dy = way_to_coord[way]
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or (board[nx][ny][0] == 0 and board[nx][ny][1] != -1):
                continue
            board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
            break
    return 0

def dfs(board, eaten_num, shark, d):
    # 물고기 움직이고
    move_fishes(board)
    # 상어가 갈 수 있는 후보도착지들
    x, y = shark
    _, way = board[x][y]
    dx, dy = way_to_coord[way]
    targets = []
    for _ in range(4):
        nx, ny = x + dx, y + dy
        x, y = nx, ny
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
            continue
        if board[nx][ny][1] == -1:
            continue
        targets.append((nx, ny))
    # 만약 갈 곳이 없다면
    if len(targets) == 0:
        global answer
        # 만약 지금까지 먹은 물고기가, 더 많다면 저장
        if eaten_num > answer:
            answer = eaten_num
            return
    x, y = shark
    for nx, ny in targets:
        board_copy = copy.deepcopy(board)
        eaten_num_copy = copy.copy(eaten_num)
        eaten_fish_num = board_copy[nx][ny][0]
        board_copy[nx][ny][0] = 0
        board_copy[x][y][1] = -1
        eaten_num_copy += eaten_fish_num
        dfs(board_copy, eaten_num_copy, (nx, ny), d + 1)
    return 0


sys.stdin = open("19236_청소년_상어.txt", "r")
way_to_coord = {1: (-1, 0), 2: (-1, -1), 3: (0, -1), 4: (1, -1), 5: (1, 0), 6: (1, 1), 7: (0, 1), 8: (-1, 1)}

origin_board = []
for _ in range(4):
    tmp = list(map(int, input().split()))
    row = []
    for i in range(0, 7, 2):
        row.append([tmp[i], tmp[i + 1]])
    origin_board.append(row)



# 상어 침입
eaten_fish_num = origin_board[0][0][0]
origin_board[0][0][0] = 0
# 최고 물고기 섭취 수
answer = 0
dfs(origin_board, eaten_fish_num, (0, 0), 0)
print(answer)
