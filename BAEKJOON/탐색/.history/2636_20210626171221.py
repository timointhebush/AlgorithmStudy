# 입력을 받아, 치즈 형태와 방문을 확인할 수 있는 행렬 생성
size = input().split(" ")
row_size, col_size = int(size[0]), int(size[1])
board, visit_board, queue = [], [], []
for i in range(row_size):
    board.append(input().split(" "))
    visit_board.append([False for j in range(col_size)])
