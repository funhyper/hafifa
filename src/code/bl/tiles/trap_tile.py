from code.bl.tiles.abstract.tile_base import TileBase
from code.bl.util.move import Move
from code.bl.util.move_calculator import MoveCalculator
from code.bl.util.point import Point


class TrapTile(TileBase):
    def __init__(self, move_calculator: MoveCalculator, player: PlayerEntity, entity: EntityBase = None,
                 trap_damage: int=10):
        super().__init__(entity)
        self.move_calculator = move_calculator
        self.player = player
        self.trap_damage = trap_damage

    def get_point_after_move(self, player_point: Point, move: Move) -> Point:
        self.player.accept_damage(self.trap_damage)
        return self.move_calculator.get_point_after_move(player_point, move)
