def solution(board, moves):
    answer = 0
    n = len(board)
    new_board = {_: [] for _ in range(1, n + 1)}
    for col in range(n):
        for row in range(n - 1, -1, -1):
            if board[row][col] == 0:
                break
            new_board[col + 1].append(board[row][col])
    basket = []
    for move in moves:
        if len(new_board[move]) != 0:
            basket.append(new_board[move].pop())
        if len(basket) >= 2 and basket[-1] == basket[-2]:
            basket.pop()
            basket.pop()
            answer += 2
    return answer


print(
    solution(
        [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
        [1, 5, 3, 5, 1, 2, 1, 4],
    )
)
