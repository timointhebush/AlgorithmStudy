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


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
def roll_east():
    dice[0][0], dice[1][0], dice[1][1], dice[1][2] = dice[1][0], dice[1][1], dice[1][2], dice[0][0]


def roll_west():
    dice[0][0], dice[1][0], dice[1][1], dice[1][2] = dice[1][2], dice[0][0], dice[1][0], dice[1][1]

def roll_north():
    dice[0][0], dice[0][1], dice[1][1], dice[2][1] = dice[2][1], dice[0][0], dice[0][1], dice[1][1]

def roll_south():
    dice[0][0], dice[0][1], dice[1][1], dice[2][1] = dice[0][1], dice[1][1], dice[2][1], dice[0][0]


sys.stdin = open("백준_주사위_굴리기.txt", "r")



N, M, x, y, K = tuple(map(int, input().split()))
board = []
for n in range(N):
    row = list(map(int, input().split()))
    board.append(row)
commands = list(map(int, input().split()))
dice = [[0 for _ in range(3)] for _ in range(3)]

roll_dict = {1: roll_east, 2: roll_west, 3: roll_north, 4: roll_south}
coord_dict = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}

for i, command in enumerate(commands):
    # print(i, '번째 커맨드: ', command)
    dx, dy = coord_dict[command]
    nx, ny = x + dx, y + dy
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
    x, y = nx, ny
    roll_dict[command]()
    if board[x][y] != 0:
        dice[1][1] = board[x][y]
        board[x][y] = 0
    else:
        board[x][y] = dice[1][1]
    # print("주사위")
    # for _ in dice:
    #     print(_)
    # print("지도")
    # for _ in board:
    #     print(_)
    # print("주사위 좌표", x, y)
    print(dice[0][0])



# T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    # ///////////////////////////////////////////////////////////////////////////////////
