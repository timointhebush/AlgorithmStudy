from itertools import permutations


def solution(board, r, c):
    answer = 0
    card_coords = []
    for i, row in enumerate(board):
        for j, card in enumerate(row):
            if card != 0:
                card_coords.append((i, j))
    coords_permutations = permutations(card_coords, len(card_coords))
    print(list(coords_permutations)[0])
    # TODO: 첫번째 커서 위치를 고려하는 경우 추가
    for coords_case in coords_permutations:
        for i in range(len(coords_case) - 1):
            cur_r, cur_c = coords_case[i]
            nxt_r, nxt_c = coords_case[i + 1]
            if board[cur_r][cur_c] != board[nxt_r][nxt_c]:
                break



    return answer

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))