from code.bl.util.move import Move
from code.bl.util.point import Point


class MoveCalculator:
    def get_point_after_move(self, initial_point: Point, move: Move) -> Point:
        if move == Move.UP:
            return Point(initial_point.x + 1, initial_point.y)
        elif move == Move.DOWN:
            return Point(initial_point.x - 1, initial_point.y)
        elif move == Move.LEFT:
            return Point(initial_point.x, initial_point.y - 1)
        return Point(initial_point.x, initial_point.y + 1)