size = input().split(" ")
row_size, col_size = int(size[0]), int(size[1])
board = []
visit_board = []
queue = []
# 판과, 방문한 판 생성
for i in range(row_size):
    row = input().split(" ")
    board.append(row)
    visit_board.append([False for i in range(col_size)])

visit_board[0][0] = True
queue.append((0, 0))
row_move, col_move = [1, 0, -1], [1, 0, -1]
melted_level, hour = [], 0
all_melted = False

while all_melted == False:
    while len(queue) != 0:
        melted = 0
        hour += 1
        row, col = queue.pop(0)
        for i in row_move:
            for j in col_move:
                if i==0 and j==0:
                    break
                next_row, next_col = row+i, col+j
                if next_row >= 0 and next_row < row_size and next_col >=0 and next_col < col_size:
                    if visit_board[next_row][next_col] == False:
                        visit_board[next_row][next_col] = True
                        # 방문하지 않은곳
                        if board[next_row][next_col] == "1":
                            # 방문한 곳이 치즈
                            board[next_row][next_col] = "0"
                            melted += 1
                        else:
                            # 치즈가 아닌
                            queue.append((next_row, next_col)) #큐에 추가.
        if melted == 0:
            all_melted = True
        else:
            melted_level.append(melted)
print(hour)
print(melted_level[-1])

                

