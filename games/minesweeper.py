import typing as t
from dataclasses import dataclass
import itertools 
import random
import collections

@dataclass
class Cell: 
    is_a_mine: bool = False
    mines_around: int = 0
    hidden: bool = True

    def __repr__(self): 
        return str((self.mines_around, self.is_a_mine))

Board: t.TypeAlias = list[list[Cell]]
Coord: t.TypeAlias = tuple[int, int]

OFFSETS = [-1, 0, 1]
DIRECTIONS = list(itertools.product(OFFSETS, OFFSETS))
DIRECTIONS.remove((0, 0))

def cells_around(coordinate: Coord, board_size: int) -> t.Iterator[Coord]:
    r, c = coordinate
    for dr, dc in DIRECTIONS: 
        ro, co = r + dr, c + dc 
        if not (ro < 0 or co < 0 or ro >= board_size or co >= board_size): 
            yield ro, co


def create_board(number_of_mines: int, board_size: int) -> Board: 
    idxs = range(board_size)
    positions = list(itertools.product(idxs, idxs))
    mine_positions = set(random.sample(positions, k=number_of_mines))
    board = [[Cell(is_a_mine=((r, c) in mine_positions)) for r in range(board_size)] for c in range(board_size)]

    for r in range(board_size): 
        for c in range(board_size): 
            surrounding = 0
            for ro, co in cells_around((r, c), board_size):
                cell = board[ro][co] 
                if cell.is_a_mine: 
                    surrounding += 1
            board[r][c].mines_around = surrounding
    
    return board


board = create_board(2, 4)
print(board)



def play(chosen: Coord, board: Board) -> None: 
    r, c = chosen 
    if board[r][c].hidden: 
        return 
    if board[r][c].is_a_mine: 
        raise Exception("wah wah wah lost game")
    
    board[r][c].hidden = False
    if board[r][c].mines_around == 0:
        q = collections.deque([chosen])
        while q: 
            coord = q.popleft()
            for ro, co in cells_around(coord, len(board)):
                if board[ro][co].mines_around == 0:
                    q.append((ro, co))
                    board[ro][co].hidden = False
