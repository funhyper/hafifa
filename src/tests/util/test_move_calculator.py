import pytest

from code.bl.util.move import Move
from code.bl.util.move_calculator import MoveCalculator
from code.bl.util.point import Point


@pytest.fixture
def move_calculator() -> MoveCalculator:
    return MoveCalculator()


@pytest.mark.parametrize("point, move, expected", [
    (Point(0,0), Move.UP, Point(0, 1)),
    (Point(0,0), Move.DOWN, Point(-1, 1)),
    (Point(0,0), Move.RIGHT, Point(1, 0)),
    (Point(0,0), Move.LEFT, Point(-1, 0)),
])
def test__get_point_after_move__sanity(move_calculator, point: Point, move: Move, expected: Point):
    # Act
    new_point = move_calculator.get_point_after_move(point, move) == expected
    # Assert
    assert new_point == expected