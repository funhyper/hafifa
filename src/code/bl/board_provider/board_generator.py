from code.bl.board_provider.abstract.board_provider_base import BoardProviderBase
from code.bl.game_board.game_board import GameBoard
from code.bl.util.point import Point


class BoardGenerator(BoardProviderBase):
    def __init__(self, tile_generator, board_size: Point):
        self.tile_generator = tile_generator
        self.board_size = board_size

    def get_board(self) -> GameBoard:
        board = dict()
        for x in range(self.board_size.x):
            for y in range(self.board_size.y):
                board[Point(x, y)] = self.tile_generator.get_random_tile()
        return GameBoard(board)
