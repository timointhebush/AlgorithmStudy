class Square():
    def __init__(self, color):
        self.color = color
        self.pieces = []
    
    def __str__(self):
        return self.pieces
    
    def stack(self, piece):
        self.pieces.append(piece)
    
    def getNumStacked(self):
        return len(self.pieces)
    
    def turnPieces(self):
        self.pieces.reverse()

    def getBottom(self):
        return self.pieces[0]
    
    def getPiecesIdx(self):
        idx = []
        for piece in self.pieces:
            idx.append(piece.id)
        return idx

class Piece():
    def __init__(self, id, dir):
        self.id = id
        self.dir = dir
    
    def __str__(self):
        return "id: {}".format(self.id)
    
    def turnDir(self):
        if self.dir == 1:
            self.dir = 2
        elif self.dir == 2:
            self.dir = 1
        elif self.dir == 3:
            self.dir = 4
        else:
            self.dir = 3

def getNextCoor(row, col, dir):
    if dir == 1:
        return (row, col + 1)
    elif dir == 2:
        return (row, col-1)
    elif dir == 3:
        return (row-1, col)
    else:
        return (row+1, col)

def checkOutofRange(row, col, N):
    if row < 0 or row >= N or col < 0 or col >= N:
        return True
    else:
        return False

def move(square, board, row, col, nxtRow, nxtCol):
    idxes = square.getPiecesIdx()
    for idx in idxes:
        piecePos[idx] = (nxtRow, nxtCol)
    piecePos[idx] = (nxtRow, nxtCol)
    board[nxtRow][nxtCol].pieces += board[row][col].pieces
    board[row][col].pieces = []

def getColor(row, col, dir):
    nxtRow, nxtCol = getNextCoor(row, col, dir)
    # 해당 좌표가 체스보드 범위를 벗어나는지 체크
    if checkOutofRange(nxtRow, nxtCol, N):
        color = 2
    else:
        color = board[nxtRow][nxtCol].color

# 체스판의 크기, 말의 개수 입력
tmp = input().split(" ")
N, K = int(tmp[0]), int(tmp[1])

# 체스판 입력
board = []
for i in range(N):
    tmp = list( map( int, input().split(" ") ) )
    squareList = []
    for j, color in enumerate(tmp):
        squareList.append(Square(color))
    board.append(squareList)

piecePos = []

for i in range(K):
    tmp = list( map( int, input().split(" ") ) )
    row, col = tmp[0]-1, tmp[1]-1
    piecePos.append( ( row, col ) )
    board[row][col].stack(Piece(i, tmp[2]))

for b in board:
    print(b) 
print(piecePos)

ans = -1
for turn in range(1, 1001):
    for idx in range(K):
        row, col = piecePos[idx]
        square = board[row][col]
        print('turn : ', turn, 'idx : ', idx ,square.pieces)
        piece = square.getBottom()
        # 1. 해당 말이 가장 바닥에 있는지 확인한다.
        if piece.id == idx: #바닥이므로 움직임 가능
            # 해당 말이 움직일 곳의 타일의 색을 확인한다.
            color = getColor(row, col, piece.dir)
            # 각 타일에 대한 조치 후 움직임.
            if color <= 1: #하얀, 빨간
                if color == 1: # 빨간
                    square.turnPieces()
                move(square, board, row, col, nxtRow, nxtCol)
            else: # color == 2 파란색 혹은 범위 밖
                piece.turnDir()
                color = getColor(row, col, piece.dir)
                if color < 2:
                    move(square, board, row, col, nxtRow, nxtCol)
                    if color == 1:
                        board[nxtRow][nxtCol].turnPieces()
            # 말을 이동하고, 갯수가 4개가 넘었는지 확인함.
            if board[nxtRow][nxtCol].getNumStacked() >= 4:
                ans = turn
                break       
        else: #움직임 불가능
            pass
    if ans != -1:
        break
    print(piecePos)
print(ans)

