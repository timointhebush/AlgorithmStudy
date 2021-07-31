from collections import deque

def solution(board):
    n = len(board)
    queue = deque()
    queue.append((0, 0, 0, 2))
    queue.append((0, 0, 0, 3))
    visited = {(0,0,2):True, (0,0,3):True}
    moves = [ (-1, 0), (1, 0), (0, -1), (0, 1) ]
    while len(queue) != 0:
        row, col, cost ,dirc = queue.popleft()
        for move in moves:
            m_row, m_col = move
            n_row, n_col = row + m_row, col + m_col
            if n_row < 0 or n_col < 0 or n_row >= n or n_col >= n or (n_row, n_col, dirc) in visited:
                break
            visited[ (n_row, n_col, dirc) ] = True
            

    visited = {}
    ans_board = [ [  ]   ]
    answer = 0
    return answer
