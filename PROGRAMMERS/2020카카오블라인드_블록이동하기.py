def solution(board):
    from collections import deque
    answer = 0
    n = len(board)
    # tuple의 0번째를 tail, 1번째를 head
    timeBoard = [ [float('inf') for _ in range(n)] for _ in range(n) ]
    queue = deque( [ ( (0,0), (0,1), 0 ) ] )
    visited = set( ( (0,0), (0,1), 0 ) )
    while len(queue) != 0:
        start = queue.popleft()
        nextMoves = getNextMoves(start, board)
        if nextMoves:
            for connected in nextMoves:
                if connected not in visited:
                    updateTimeBoard(timeBoard, connected)
                    queue.append(connected)
                    visited.add( ( connected[0], connected[1] ) )
        for b in timeBoard:
            print(b)
        print("  ")
        print(visited)
    return timeBoard[-1][-1]

def getNextMoves(robot, board):
    nextMoves = getParallerMoves(robot, board) + getRotateMoves(robot, board)
    nextMoves = filterMoves(nextMoves, board)
    return nextMoves

def getParallerMoves(robot, board):
    partA, partB, time = robot
    moves = []
    #up
    moves.append( ( (partA[0]-1, partA[1]), (partB[0]-1, partB[1]), time+1 ) )
    #down
    moves.append( ( (partA[0]+1, partA[1]), (partB[0]+1, partB[1]), time+1 ) )
    #left
    moves.append( ( (partA[0], partA[1]-1), (partB[0], partB[1]-1), time+1 ) )
    #right
    moves.append( ( (partA[0], partA[1]+1), (partB[0], partB[1]+1), time+1 ) )
    return moves

def getRotateMoves(robot, board):
    partA, partB, time = robot
    if partA[0] == partB[0]: # 가로 방향
        moves = getHorizonRotate(robot, board)
    else:
        moves = getVerticalRoatae(robot, board)
    return moves

def getHorizonRotate(robot, board):
    partA, partB, time = robot
    moves = []
    if isCoordOut(partA[0]-1, partA[1]+1, board) == False and board[partA[0]-1][partA[1]+1] != 1:
        moves.append( ( (partA[0], partA[1]), (partB[0]-1, partB[1]-1), time+1 ) )
    if isCoordOut(partA[0]+1, partA[1]+1, board) == False and board[ partA[0]+1 ][ partA[1]+1 ] != 1:
        moves.append( ( (partA[0], partA[1]), (partB[0]+1, partB[1]-1), time+1 ) )
    if isCoordOut( partB[0]-1 , partB[1]-1, board) == False and board[ partB[0]-1 ][ partB[1]-1 ] != 1:
        moves.append( ( (partA[0]-1, partA[1]+1), (partB[0], partB[1]), time+1 ) )
    if isCoordOut( partB[0]+1 , partB[1]-1, board ) == False and board[ partB[0]+1 ][ partB[1]-1 ] != 1:
        moves.append( ( (partA[0]+1, partA[1]+1), (partB[0], partB[1]), time+1 ) )
    return moves

def getVerticalRoatae(robot, board):
    partA, partB, time = robot
    moves = []
    if isCoordOut(partA[0]+1, partA[1]+1, board) == False and board[partA[0]+1][partA[1]+1] != 1:
        moves.append( ( (partA[0], partA[1]), (partB[0]-1, partB[1]+1), time+1 ) )
    if isCoordOut(partA[0]+1, partA[1]-1, board) == False and board[ partA[0]+1 ][ partA[1]-1 ] != 1:
        moves.append( ( (partA[0], partA[1]), (partB[0]-1, partB[1]-1), time+1 ) )
    if isCoordOut(partB[0]-1 , partB[1]+1, board) == False and board[partB[0]-1 ][ partB[1]+1] != 1:
        moves.append( ( (partA[0]+1, partA[1]+1), (partB[0], partB[1]), time+1 ) )
    if isCoordOut(partB[0]-1 , partB[1]-1, board) == False and board[partB[0]-1 ][ partB[1]-1] != 1:
        moves.append( ( (partA[0]+1, partA[1]-1), (partB[0], partB[1]), time+1 ) )
    return moves

def isCoordOut(row, col, board):
    n = len(board)
    if row < 0 or col < 0 or row >= n or col >= n:
        return True
    return False

def isCoordWall(row, col, board):
    if isCoordOut(row, col, board):
        return True
    if board[row][col] == 1:
        return True
    return False

def filterMoves(nextMoves, board):
    moves = []
    for move in nextMoves:
        partA, partB, time = move
        if isCoordOut(partA[0], partA[1], board) or isCoordOut(partB[0], partB[1], board) or isCoordWall(partA[0], partA[1], board) or isCoordWall(partB[0], partB[1], board):
            pass
        else:
            moves.append(move)
    return moves

def isLessThan(timeBoard, connected):
    partA, partB, time = connected
    if timeBoard[partA[0]][partA[1]] >= time or timeBoard[partB[0]][partB[1]] >= time:
        return True
    return False

def updateTimeBoard(timeBoard, connected):
    partA, partB, time = connected
    timeBoard[partA[0]][partA[1]] = time
    timeBoard[partB[0]][partB[1]] = time

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))