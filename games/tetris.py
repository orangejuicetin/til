class Tetris:
    def __init__(self, nrows=20, ncols=10):
        self.nrows = nrows
        self.ncols = ncols
        self.reset()

    def reset(self):
        self.board = [[None] * self.ncols for _ in range(self.nrows)]
        self.lost = False
        self.pause = False

    def piece_can_go_here(self, pos) -> bool:
        return all(
            0 <= r < self.nrows and 0 <= c < self.ncols and not self.board[r][c]
            for (r, c) in pos
        )

    def find_completed_rows(self):
        pass
