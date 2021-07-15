class Horse():
    def __init__(self, id, pos, dir):
        super().__init__()
        self.id = id
        self.dir = dir
        self.isOnTopOf = pos
        self.liesBelow = 0
    
    def move(self):
        if type(self.isOnTopOf) == tuple:
            if self.dir == 1:
                self.isOnTopOf = (self.isOnTopOf[0], self.isOnTopOf[1]+1)
            elif self.dir == 2:
                self.isOnTopOf = (self.isOnTopOf[0], self.isOnTopOf[1]-1)
            elif self.dir == 3:
                self.isOnTopOf = (self.isOnTopOf[0]-1, self.isOnTopOf[1])
            else: #self.dir == 4:
                self.isOnTopOf = (self.isOnTopOf[0]+1, self.isOnTopOf[1])
            return self.isOnTopOf
        else:
            return None

    def moveBack(self):
        if type(self.isOnTopOf) == tuple:
            if self.dir == 1:
                self.isOnTopOf = (self.isOnTopOf[0], self.isOnTopOf[1]-1)
            elif self.dir == 2:
                self.isOnTopOf = (self.isOnTopOf[0], self.isOnTopOf[1]+1)
            elif self.dir == 3:
                self.isOnTopOf = (self.isOnTopOf[0]+1, self.isOnTopOf[1])
            else: #self.dir == 4:
                self.isOnTopOf = (self.isOnTopOf[0]-1, self.isOnTopOf[1])
            return self.isOnTopOf
        else:
            return None

class Chessboard():
    def __init__(self, board):
        super().__init__()
        self.board = board
        self.horseBoard = [[0 for i in range(len(board))] for j in range(len(board))]

class Game():
    def __init__(self, chessboard, horseList, numOfHorses):
        super().__init__()
        self.chessboard = chessboard
        self.horseList = horseList
        self.turn = 0
        self.numOfHorses = numOfHorses
        for horse in horseList:
            row, col = horse.isOnTopOf
            self.chessboard.horseBoard[row][col] = horse.id

    def checkColor(self, pos):
        row, col = pos
        n = len(self.chessboard.board) - 1
        if row < 1 or row > n or col < 1 or col > n:
            return 3
        return self.chessboard.board[row][col]

    def move(self):
        moveTo = self.horseList[self.turn].move()

        if moveTo != None:
            spaceColor = self.checkColor((moveTo[0], moveTo[1]))
            if spaceColor == 0:
                bottomHorse = self.horseList[self.turn]
            elif spaceColor == 1:
                bottomHorse = self.spaceRed(self.horseList[self.turn])
            elif spaceColor >= 2:
                bottomHorse = self.spaceBlue(self.horseList[self.turn])
                pos = bottomHorse.isOnTopOf
                if self.checkColor(pos) >= 2:
                    bottomHorse.moveBack()
            self.stackHorseTo(bottomHorse.isOnTopOf, bottomHorse)

        self.turn = (self.turn + 1) % self.numOfHorses

    def stackHorseTo(self, pos, horse):
        row, col = pos
        horseId = self.chessboard.horseBoard[row][col]
        if horseId == 0:
            self.chessboard.horseBoard[row][col] = horse.id
        else:
            bottomHorse = self.horseList[horseId-1]
            while bottomHorse.liesBelow != 0:
                bottomHorse = bottomHorse.liesBelow
            bottomHorse.liesBelow = horse
            

    def spaceRed(self, horse):
        stackedHorses = [horse]
        upperHorse = horse.liesBelow
        while upperHorse != 0:
            stackedHorses.append(upperHorse)
            upperHorse = upperHorse.liesBelow
        
        numOfStacked = len(stackedHorses)
        if numOfStacked != 1:
            pos = stackedHorses[0].isOnTopOf
            stackedHorses[-1].isOnTopOf = pos
            stackedHorses[-1].liesBelow = stackedHorses[-2]

            for i in range(len(stackedHorses)-1, -1):
                if i == 0:
                    stackedHorses[i].isOnTopOf = stackedHorses[i+1]
                    stackedHorses[i].liesBelow = 0 
                stackedHorses[i].isOnTopOf = stackedHorses[i+1]
                stackedHorses[i].liesBelow = stackedHorses[i-1]
        bottomHorse = stackedHorses[-1]
        return bottomHorse
    
    def spaceBlue(self, horse):
        if horse.dir == 1:
            horse.dir = 2
        elif horse.dir == 2:
            horse.dir = 1
        elif horse.dir == 3:
            horse.dir = 4
        else:
            horse.dir = 3
        horse().move()
        return horse
    
    def checkStackedHorses(self):
        for horse in self.horseList:
            if type(horse.isOnTopOf) == tuple:
                num = 0
                upperHorse = horse.liesBelow
                while upperHorse != 0:
                    num += 1
                    upperHorse = upperHorse.liesBelow
                    if num >= 4:
                        return True
        return False
        
tmp = input().split(" ")
N, K = int(tmp[0]), int(tmp[1])
board = [[0 for i in range(N+1)]]
for i in range(N):
    tmp = input().split(" ")
    tmp.insert(0, '0')
    tmp = list(map(int, tmp))
    board.append(tmp)
chessboard = Chessboard(board)

horseList = []
for i in range(K):
    tmp = list(map(int, input().split(" ")))
    horseList.append(Horse(i+1, (tmp[0], tmp[1]), tmp[2]))

game = Game(chessboard, horseList, K)
ans = 0
status = False
for i in range(1000):
    game.move()
    status = game.checkStackedHorses()
    if status == True:
        ans = i+1
        break
if status == True:
    print(ans)
else:
    print(-1)