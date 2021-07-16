class Horse():
    def __init__(self, id, dir):
        self.id = id
        self.dir = dir
        self.onTop = None

class Square():
    def __init__(self, color):
        self.color = color
        self.onTop = None

class Chessboard():
    def __init__(self, board, horsePos):
        self.board = board
        self.horsePos = horsePos

    def checkHorseBottom(self, horseIdx):
        row, col = self.horsePos[horseIdx]
        return self.board[row][col].onTop.id == horseIdx
    
    def getMove(self, dir):
        if dir == 1:
            return (0, 1)
        elif dir == 2:
            return (0, -1)
        elif dir == 3:
            return (-1, 0)
        else:
            return (1, 0)
    
    def getTopOfSquare(self, square):
        lowerSquare = square
        upperSquare = square.onTop
        while upperSquare != None:
            lowerSquare = upperSquare
            upperSquare = upperSquare.onTop
        return lowerSquare
    
    def whenRed(self, horseIdx):
        row, col = self.horsePos[horseIdx]
        movingHorse = self.board[row][col].onTop
        horseList = [movingHorse]
        while movingHorse.onTop != None:
            movingHorse = movingHorse.onTop
            horseList.append(movingHorse)
        
        n = len(horseList)
        self.horsePos[horseList[-1].id] = (row, col)
        self.board[row][col].onTop = horseList[-1]
        
        for i in range(n-1, 0, -1):
            horseList[i].onTop = horseList[i-1]
        horseList[0].onTop = None
        
    def moveHorse(self, horseIdx):
        if self.checkHorseBottom(horseIdx) == False:
            return False
        row, col = self.horsePos[horseIdx]
        movingHorse = self.board[row][col].onTop
        dir = movingHorse.dir
        moveRow, moveCol = self.getMove(dir)
        
        self.board[row][col].onTop = None
        topOfSquare = self.getTopOfSquare(self.board[row+moveRow][col+moveCol])
        topOfSquare.onTop = movingHorse
        self.horsePos[horseIdx] = ( row+moveRow, col+moveCol )
        return( row+moveRow, col+moveCol )

# 체스판의 크기, 말의 개수 입력
tmp = input().split(" ")
N, K = int(tmp[0]), int(tmp[1])

# 체스판 입력
board = []
for i in range(N):
    tmp = list( map( int, input().split(" ") ) )
    tmp2 = []
    for j in tmp:
        tmp2.append(Square(j))
    board.append(tmp2)

# 말 정보 입력
horsePos = []
for i in range(K):
    tmp = list( map( int, input().split(" ") ) )
    board[tmp[0]-1][tmp[1]-1].onTop = Horse(i, tmp[2])
    horsePos.append( (tmp[0]-1, tmp[1]-1) )

chessboard = Chessboard(board, horsePos)

chessboard.moveHorse(0)

print(chessboard.board[1][1].onTop.id)

