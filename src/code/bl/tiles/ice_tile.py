from code.bl.entities.entity import Entity
from code.bl.tiles.abstract.tile_base import TileBase
from code.bl.util.move import Move
from code.bl.util.move_calculator import MoveCalculator
from code.bl.util.point import Point


class IceTile(TileBase):
    def __init__(self, move_calculator: MoveCalculator, on_tile_entity: Entity = None,
                 skipped_tiles_count: int = 2):
        super().__init__(on_tile_entity)
        self.move_calculator = move_calculator
        self.skipped_tiles_count = skipped_tiles_count

    def get_point_after_move(self, player_point: Point, move: Move) -> Point:
        player_final_point = self.move_calculator.get_point_after_move(player_point, move)
        for _ in range(self.skipped_tiles_count - 1):
            player_final_point = self.move_calculator.get_point_after_move(player_point, move)
        return player_final_point
