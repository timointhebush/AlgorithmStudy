def solution(board):
    from collections import deque
    answer = 0
    # tuple의 0번째를 tail, 1번째를 head
    robot = ( (0,0), (0,1) )
    queue = deque( getNextMoves() )
    while len(queue) != 0:
        


    return answer

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))