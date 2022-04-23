import sys

input = sys.stdin.readline


class BoardGame:
    def __init__(self, board, red, blue, hole):
        self.N, self.M = len(board), len(board[0])
        self.board = board
        self.red_stack = []
        self.blue_stack = []
        self.red = red
        self.blue = blue
        self.hole = hole
        self.count = 0

    def _is_game_over(self, coord):
        if coord == self.hole:
            return True
        else:
            return False

    def _is_hit_wall(self, coord):
        r, c = coord
        if self.board[r][c] == "#":
            return True
        else:
            return False

    def _is_overlap(self, A, B):
        if A == B:
            return True
        else:
            return False

    def _get_dir_coord(self, direction):
        if direction == "R":
            return (0, 1)
        elif direction == "L":
            return (0, -1)
        elif direction == "U":
            return (-1, 0)
        else:
            return (1, 0)

    def _coord_sum(self, A, B):
        return (A[0] + B[0], A[1] + B[1])

    def _move_one_step(self, direction):
        coord = self._get_dir_coord(direction)
        prev_red, prev_blue = self.red, self.blue
        next_red, next_blue = self._coord_sum(self.red, coord), self._coord_sum(self.blue, coord)
        hitted_red, hitted_blue = False, False
        if self._is_hit_wall(next_red):
            next_red = prev_red
            hitted_red = True
        if self._is_hit_wall(next_blue):
            next_blue = prev_blue
            hitted_blue = True

        if self._is_overlap(next_red, next_blue):
            if hitted_blue:
                next_red = prev_red
            elif hitted_red:
                next_blue = prev_blue
            else:
                print("예외")
        self.red, self.blue = next_red, next_blue

    def lean(self, direction):
        if direction == 'U' or direction == 'D':
            repeat_n = self.N - 2
        else:
            repeat_n = self.M - 2
        self.red_stack.append(self.red)
        self.blue_stack.append(self.blue)
        for _ in range(repeat_n):
            self._move_one_step(direction)
            if self._is_game_over(self.red):
                raise BaseException()
        self.count += 1


if __name__ == "__main__":
    N, M = tuple(map(int, input().split()))
    board = []
    red, blue = (0, 0), (0, 0)
    hole = (0, 0)
    for n in range(N):
        row = input().split()
        for m in range(M):
            if row[m] == "B":
                blue = (n, m)
            elif row[m] == "R":
                red = (n, m)
            elif row[m] == "O":
                hole = (n, m)
        board.append(row)
    board_game = BoardGame(board, red, blue, hole)
    dir_list = ["U", "D", "R", "L"]
    counts = []
    stack = []
    visited = set()
    for direction in dir_list:
        stack.append((board_game.count, direction))
        visited.add((board_game.count, direction))
    while stack:
        _, direction = stack.pop()
        try:
            board_game.lean(direction)
        except BaseException():
            counts.append(board_game.count)

