def solution(board):
    from collections import deque
    n = len(board)
    # 겉면을 1로 감싸는 new_board 생성
    new_board = [ [ 1 for _ in range(n+2) ] for _ in range(n+2) ]
    for row in range(1, n+1):
        for col in range(1, n+1):
            new_board[row][col] = board[row-1][col-1]
    import copy
    time_board = copy.deepcopy(new_board)
    queue = deque( [ ( (1, 1), (1, 2), 0 ) ] )
    visited = set([ ((1, 1), (1, 2)) ])
    time = 0
    while queue:
        partA, partB, time = queue.popleft()
        if partA == (n, n) or partB == (n, n):
            return time
        next_moves = getNextMoves(partA, partB, new_board)
        # print(time, ":", next_moves)
        for n_partA, n_partB in next_moves:
            if ( n_partA, n_partB ) not in visited:
                visited.add( (n_partA, n_partB) )
                queue.append( ( n_partA, n_partB, time+1 ) )
                time_board[ n_partA[0] ][ n_partA[1] ] = time + 1
                time_board[ n_partB[0] ][ n_partB[1] ] = time + 1
        # for i in time_board:
        #     print(i)
        # print("")

def getNextMoves(partA, partB, new_board):
    next_moves = []
    parallel_move = [ (1,0), (-1,0), (0, 1), (0, -1) ]
    for d_row, d_col in parallel_move:
        if new_board[ partA[0]+d_row ][ partA[1]+d_col ] != 1 and new_board[ partB[0]+d_row ][ partB[1]+d_col ] != 1:
            next_moves.append( (( partA[0]+d_row, partA[1]+d_col ), ( partB[0]+d_row, partB[1]+d_col )) )
    
    if partA[0] == partB[0]: # 가로
        UP, DOWN = -1, 1
        for dire in [UP, DOWN]:
            if new_board[ partA[0]+dire ][ partA[1] ] != 1 and new_board[ partB[0]+dire ][ partB[1] ] != 1:
                next_moves.append( ( partA, (partA[0]+dire, partA[1]) ) )
                next_moves.append( (  partB, (partB[0]+dire, partB[1]) ) )
    else: # 세로
        LEFT, RIGHT = -1, 1
        for dire in [LEFT, RIGHT]:
            if new_board[ partA[0] ][ partA[1]+dire ] != 1 and new_board[ partB[0] ][ partB[1]+dire ] != 1:
                next_moves.append( ( (partA[0], partA[1]+dire), partA ) ) 
                next_moves.append( ( (partB[0], partB[1]+dire), partB ) )
    return next_moves

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))