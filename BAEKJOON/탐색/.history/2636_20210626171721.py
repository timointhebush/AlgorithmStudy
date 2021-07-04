# 입력을 받아, 치즈 형태와 방문을 확인할 수 있는 행렬 생성
# BFS를 위한 큐 생성.
size = input().split(" ")
row_size, col_size = int(size[0]), int(size[1])
board, visit_board, queue = [], [], []
for i in range(row_size):
    board.append(input().split(" "))
    visit_board.append([False for j in range(col_size)])

# 치즈의 한 겉면을 확인하기 위한 한 사이클 코드
queue.append((0, 0))
copy_visit_b = visit_board.copy() # 매 사이클마다 방문 기록이 초기화되게 하기 위해.
copy_visit_b[0][0] = True
while len(queue) != 0:
    