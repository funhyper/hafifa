from code.bl.entities.abstract.monster_base import MonsterBase
from code.bl.entities.entity import Entity
from code.bl.tiles.abstract.tile_base import TileBase
from code.bl.util.move import Move
from code.bl.util.move_calculator import MoveCalculator
from code.bl.util.point import Point


class TrapTile(TileBase):
    def __init__(self, move_calculator: MoveCalculator, player: Entity, on_tile_entity: MonsterBase = None,
                 trap_damage: int = 10):
        super().__init__(on_tile_entity)
        self.move_calculator = move_calculator
        self.player = player
        self.trap_damage = trap_damage

    def get_point_after_move(self, player_point: Point, move: Move) -> Point:
        self.player.damage_entity(self.trap_damage)
        return self.move_calculator.get_point_after_move(player_point, move)
