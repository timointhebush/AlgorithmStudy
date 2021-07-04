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
    row, col = queue.pop(0)
    connected = [(row, col), (row, col), (row, col), (row, col)]
    # 해당 정점에 연결된 정점들을 돌면서:

        # 만약 아직 방문하지 않았다면:
            # 방문 표시
            # 큐에 추가.

def getConnected(row, col, row_size, col_size):
    tmp = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
    connected = []
    for tmp_row, tmp_col in tmp:
        if tmp_row < 0 or tmp_row >= row_size or tmp_col < 0 or tmp_col >= col_size:
            pass
        else:
             connected.append((tmp_row, tmp_col))
    return connected
