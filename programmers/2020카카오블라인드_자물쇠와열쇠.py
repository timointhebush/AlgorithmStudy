def solution(key, lock):
    M, N = len(key), len(lock)
    fullBoard = [ [ 0 for _ in range(2*M + N - 2) ] for _ in range(2*M + N - 2)  ]
    fullBoard = setLock(fullBoard, lock, key)
    for _ in range(4):
        key = rotateClock90(key)
        for startRow in range(M+N-1):
            for startCol in range(M+N-1):
                attachKey(fullBoard, key, startRow, startCol)
                if check(fullBoard, M, N):
                    return True
                dettachKey(fullBoard, key, startRow, startCol)
    return False

def setLock(fullBoard, lock, key):
    M, N = len(key), len(lock)
    for rowLock in range(N):
        for colLock in range(N):
            fullBoard[M-1 + rowLock][M-1 + colLock] = lock[rowLock][colLock]
    return fullBoard

def attachKey(fullBoard, key, startRow, startCol):
    M = len(key)
    for rowKey in range(M):
        for colKey in range(M):
            fullBoard[startRow + rowKey][startCol + colKey] += key[rowKey][colKey]

def dettachKey(fullBoard, key, startRow, startCol):
    M = len(key)
    for rowKey in range(M):
        for colKey in range(M):
            fullBoard[startRow + rowKey][startCol + colKey] -= key[rowKey][colKey]

def check(fullBoard, M, N):
    for row in range(M-1, M+N-1):
        for col in range(M-1, M+N-1):
            if fullBoard[row][col] != 1:
                return False
    return True

def rotateClock90(key):
    M = len(key)
    newKey = [ [ 0 for _ in range(M) ] for _ in range(M) ]
    for row in range(M):
        for col in range(M):
            newKey[col][M-1-row] = key[row][col]
    return newKey

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))