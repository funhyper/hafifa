from code.bl.entities.entity import Entity
from code.bl.tiles.abstract.tile_base import TileBase
from code.bl.util.move import Move
from code.bl.util.move_calculator import MoveCalculator
from code.bl.util.point import Point


class MudTile(TileBase):
    def __init__(self, move_calculator: MoveCalculator, on_tile_entity: Entity = None, moves_stuck: int = 1):
        super().__init__(on_tile_entity)
        self.move_calculator = move_calculator
        self.moves_stuck = moves_stuck

    def get_point_after_move(self, player_point: Point, move: Move) -> Point:
        if self.moves_stuck == 0:
            return self.move_calculator.get_point_after_move(player_point, move)
        self.moves_stuck -= 1
        return player_point
