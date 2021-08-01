from collections import deque

def solution(board):
    n = len(board)
    costBoard = [ [float('inf') for j in range(n)] for i in range(n) ]
    moves = [ (-1, 0), (0, 1), (1, 0), (0, -1) ]
    queue = deque( [ (0, 0, 1, 0), (0, 0, 2, 0) ] )
    while len(queue) != 0:
        row, col, dirc, cost = queue.popleft()
        for nDirc, (mRow, mCol) in enumerate(moves):
            if nDirc == dirc:
                nCost = cost + 100
            else:
                nCost = cost + 600
            nRow, nCol = row+mRow, col+mCol
            if 0 <= nRow < n and 0 <= nCol < n and board[nRow][nCol]==0 and costBoard[nRow][nCol] >= nCost:
                queue.append( (nRow, nCol, nDirc, nCost) )
                costBoard[nRow][nCol] = nCost
    return costBoard[-1][-1]

print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))