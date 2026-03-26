import random

from code.bl.util.point import Point


class RandomProvider:
    def __init__(self, board_size: Point):
        self._board_size = board_size

    def get_random_number(self, start: int, end: int) -> int:
        return random.randint(start, end)

    def get_random_board_point(self) -> Point:
        x_point = self.get_random_number(0, self._board_size.x)
        y_point = self.get_random_number(0, self._board_size.y)
        return Point(x_point, y_point)
