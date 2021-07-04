# 어떤 정점과 연결된 정점들의 리스트를 반환하는 함수
def getConnected(row, col, row_size, col_size):
    tmp = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
    connected = []
    for tmp_row, tmp_col in tmp:
        if tmp_row < 0 or tmp_row >= row_size or tmp_col < 0 or tmp_col >= col_size:
            pass
        else:
            connected.append((tmp_row, tmp_col))
    return connected

def printGraph(graph):
    for row in graph:
        print(row)

# 울타리의 사이즈를 입력받는다.
size = input().split(" ")
row_size, col_size = int(size[0]), int(size[1])
# 입력받은 사이즈를 바탕으로 뒷마당 데이터를 입력받는다. 동시에 방문 데이터를 저장할 행렬도 생성
backyard = []
visited = []
for i in range(row_size):
    backyard.append(list(input()))
    visited.append([False for j in range(col_size)])

# BFS를 위한 큐
queue = []
total_sheep, total_wolf = 0, 0
# 임의로 시작 포인트를 정해놓음

printGraph(backyard)

# 하나의 영역을 모두 BFS로 확인하는 사이클.
for i in range(row_size):
    for j in range(col_size):
        if visited[i][j] == False and backyard[i][j] != "#":
            start_row, start_col = i, j
            sheep, wolf = 0, 0
            #기본적인 BFS사이클
            visited[start_row][start_col] = True
            queue.append((start_row, start_col))
            if backyard[start_row][start_col] == "v":
                wolf += 1
            elif backyard[start_row][start_col] == "o":
                sheep += 1
            while len(queue) != 0:
                row, col = queue.pop(0)
                connected = getConnected(row, col, row_size, col_size)
                # 해당 정점과 연결된 정점들:
                for c_row, c_col in connected:
                    # 방문하지 않은 정점이라면:
                    if visited[c_row][c_col] == False:
                        # 방문 표시
                        visited[c_row][c_col] = True
                        if backyard[c_row][c_col] == "#":
                            pass
                        else:     
                            # 큐에 추가
                            queue.append((c_row, c_col))
                            if backyard[c_row][c_col] == "v":
                                wolf += 1
                            elif backyard[c_row][c_col] == "o":
                                sheep += 1
            if sheep > wolf:
                wolf = 0
            else:
                sheep = 0
            total_sheep += sheep
            total_wolf += wolf
print(total_sheep, " ", total_wolf)