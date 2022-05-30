class Piece():
    def __init__(self, id, row, col, dir):
        self.id = id
        self.pos = (row-1, col-1)
        self.dir = dir
        self.top = None
        self.bottom = None
        self.numStacked = 1
    
    def getMove(self):
        if self.dir == 1:
            return (0, 1)
        elif self.dir == 2:
            return (0, -1)
        elif self.dir == 3:
            return (-1, 0)
        else:
            return (1, 0)

    def getOppo(self):
        if self.dir == 1:
            return 2
        elif self.dir == 2:
            return 1
        elif self.dir == 3:
            return 4
        else:
            return 3
    
    def move(self):
        self.pos = self.pos + self.getMove()
        self.top.pos = self.pos
    
    def resRed(self):
        topPiece = self.top

        self.top = None
        self.bottom = topPiece
    
    def resBlue(self):
        oldDir = self.dir
        newDir = self.getOppo()
        self.dir = newDir
        moveRow, moveCol = self.getMove()
        if row+moveRow < 0 or row+moveRow >= N or col+moveCol < 0 or col+moveCol >= N or board[row+moveRow][col+moveCol]==2:
            self.dir = oldDir
            self.move()
            self.dir = newDir

        

# 체스판의 크기, 말의 개수 입력
tmp = input().split(" ")
N, K = int(tmp[0]), int(tmp[1])

# 체스판 입력
board = []
for i in range(N):
    tmp = list( map( int, input().split(" ") ) )
    board.append(tmp)

# 말 입력
piecesList = []
for i in range(K):
    tmp = list( map( int, input().split(" ") ) )
    piecesList.append( Piece(i, tmp[0], tmp[1], tmp[2]) )

for turn in range(1, 1001):
    for idx, piece in enumerate(piecesList):
        row, col = piece.pos
        moveRow, moveCol = piece.getMove()
        if row+moveRow < 0 or row+moveRow >= N or col+moveCol < 0 or col+moveCol >= N:
            color = 2
        else:
            color = board[row+moveRow][col+moveCol]
        if color == 0: #하얀색
            pass
        elif color == 1: #빨간색
            piece.resRed()
        elif color == 2: #파란, 아웃
            piece.resBlue()
        piece.move()
        movedRow, movedCol = piece.pos
        