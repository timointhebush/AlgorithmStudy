def solution(board):
    answer = 0
    # tuple의 0번째를 tail, 1번째를 head
    robot = ( (0,0), (0,1) )
    print(getNextMoves(robot, board))
    return answer

def getNextMoves(robot, board):
    vertical = True
    tail, head = robot
    tRow, tCol = tail
    hRow, hCol = head
    nextMoves = []
    degreeMove = [(1,0), (-1,0), (0,1), (0,-1)]
    for degRow, degCol in degreeMove:
        nxtTRow, nxtTCol = tRow + degRow, tCol + degCol
        nxtHRow, nxtHCol = hRow + degRow, hCol + degCol
        if checkCoorOut((nxtTRow, nxtTCol), board) == True and checkCoorOut((nxtHRow, nxtHCol), board) == True:
            nextMoves.append(( (nxtTRow, nxtTCol),(nxtHRow, nxtHCol) ))
    nextMoves += getRotateSpace(robot, board)
    return nextMoves

def checkCoorOut(coor, board):
    n = len(board)
    row, col = coor
    if row < 0 or col < 0 or row >= n or col >= n:
        return False
    return True

def checkCoorWall(coor, board):
    row, col = coor
    if board[row][col] == 1:
        return True
    return False

def checkRobotOut(robot, board):
    tail, head = robot
    if checkCoorOut(tail, board) == True or checkCoorOut(head, board) == True:
        return True
    return False

def getRotateSpace(robot, board):
    tail, head = robot
    tRow, tCol = tail
    hRow, hCol = head
    if tRow == hRow:
        vertical = False
    if vertical == True:
        candidateEmptySpace = [ (tRow+1, tCol-1), (tRow+1, tCol+1),
                                (hRow-1, hCol-1), (hRow-1, hCol+1) ]
        candidate = [ ((tRow, tCol), (tRow, tCol-1)), 
                        ((tRow, tCol), (tRow, tCol+1)),
                        ((hRow, hCol-1), (hRow, hCol)),
                        ((hRow, hCol+1), (hRow, hCol)) ]
    else:
        candidateEmptySpace = [ (tRow-1, tCol+1), (tRow+1, tCol+1),
                                (hRow-1, hCol-1), (hRow+1, hCol-1) ]
        candidate = [ ((tRow, tCol), (tRow-1, tCol)), 
                        ((tRow, tCol), (tRow+1, tCol)),
                        ((hRow-1, hCol), (hRow, hCol)),
                        ((hRow+1, hCol), (hRow-1, hCol)) ]
    rotateSpace = []
    for i in range(4):
        freeRow, freeCol = candidateEmptySpace[i]
        if checkCoorWall((freeRow, freeCol) , board) == False:
            robotCandi = candidate[i]
            if checkRobotOut(robotCandi, board) == False:
                rotateSpace.append(robotCandi)
    print(rotateSpace)
    return rotateSpace

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))