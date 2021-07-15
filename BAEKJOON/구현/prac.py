board = []
tmp = input().split(" ")
tmp.insert(0, '0')
tmp = list(map(int, tmp))
board.append(tmp)
print(board)