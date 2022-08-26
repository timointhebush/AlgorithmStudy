def solution(board, skill):
    answer = 0
    new_board = [[0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)]
    for type, r1, c1, r2, c2, degree in skill:
        value = degree
        if type == 1:
            value *= -1
        new_board[r1][c1] += value
        new_board[r2 + 1][c2 + 1] += value
        new_board[r1][c2 + 1] -= value
        new_board[r2 + 1][c1] -= value

    for r in range(len(board)):
        for c in range(len(board[0])):
            new_board[r][c + 1] += new_board[r][c]
    for c in range(len(board[0])):
        for r in range(len(board)):
            new_board[r + 1][c] += new_board[r][c]
    for c in range(len(board[0])):
        for r in range(len(board)):
            board[r][c] += new_board[r][c]
            if board[r][c] > 0:
                answer += 1
    return answer


if __name__ == "__main__":
    print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],
                   [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))