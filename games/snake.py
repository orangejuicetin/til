import collections
import random
import itertools


# done with Rhea, 11/8/23 10:44AM
class Snake:
    DOWN = (-1, 0)
    UP = (1, 0)
    RIGHT = (0, 1)
    LEFT = (0, -1)

    #  << = + + +
    # + + + + + +
    #

    def __init__(self, size: int = 10) -> None:
        self.board = [[None for _ in range(size)] for _ in range(size)]

        ro = co = size // 2
        self.board[ro][co] = "="
        self.board[ro][co + 1] = "+"
        self.snake = collections.deque([(ro, co), (ro, co + 1)])
        self.direction = self.LEFT
        idxs = range(size)
        self.all_positions = list(itertools.product(idxs, idxs))

        self.place_another_apple()

        self.game_is_over = False
        self.has_eaten = False

    def place_another_apple(self):
        new_apple = random.choice(self.all_positions)
        while new_apple in self.snake:
            new_apple = random.choice(self.all_positions)
        self.apple = new_apple
        ar, ac = self.apple
        self.board[ar][ac] = "1"

    def tick(self):
        direction = self.read_in_arrow("keyboard.input")
        if direction:
            self.direction = direction

        head_ro, head_co = self.snake[0]
        next_ro, next_co = head_ro + self.direction[0], head_co + self.direction[1]
        next_coord = (next_ro, next_co)
        if (
            not (0 <= next_ro < len(self.board) and 0 <= next_co < len(self.board[0]))
            or next_coord in self.snake
        ):
            self.game_is_over = True
            return

        if next_coord == self.apple:
            self.apple = "#"
            self.place_another_apple()
            self.has_eaten = True

        prev_position_of = self.snake.copy()

        # alternate approach duh - just take wherever the tail was and put it where the head _used_ to be
        self.snake[0] = next_coord
        self.board[next_ro][next_co] = "="
        for i in range(1, len(self.snake)):
            old_r, old_c = self.snake[i]
            self.board[old_r][old_c] = None
            self.snake[i] = prev_position_of[i - 1]
            nr, nc = self.snake[i]
            self.board[nr][nc] = "+"

        if self.has_eaten:
            old_tail = prev_position_of[-1]
            self.snake.append(old_tail)
            tr, tc = old_tail
            self.board[tr][tc] = "+"
            self.has_eaten = False

    def read_in_arrow(self, input: str):
        pass
