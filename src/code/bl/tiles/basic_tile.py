from code.bl.tiles.abstract.tile_base import TileBase
from code.bl.util.move import Move
from code.bl.util.move_calculator import MoveCalculator
from code.bl.util.point import Point


class BasicTile(TileBase):
    def __init__(self, move_calculator: MoveCalculator, entity: EntityBase=None):
        super().__init__(entity)
        self.move_calculator = move_calculator

    def get_point_after_move(self, player_point: Point, move: Move) -> Point:
        return self.move_calculator.get_point_after_move(player_point, move)
