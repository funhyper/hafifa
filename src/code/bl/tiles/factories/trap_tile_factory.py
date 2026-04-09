from code.bl.entities.abstract.monster_base import MonsterBase
from code.bl.entities.entity import Entity
from code.bl.tiles.abstract.tile_base import TileBase
from code.bl.tiles.abstract.tile_factory_base import TileFactoryBase
from code.bl.tiles.trap_tile import TrapTile
from code.bl.util.move_calculator import MoveCalculator


class TrapTileFactory(TileFactoryBase):
    def __init__(self, move_calculator: MoveCalculator, player: Entity, trap_damage: int,
                 on_tile_entity: MonsterBase = None):
        self.on_tile_entity = on_tile_entity
        self.trap_damage = trap_damage
        self.player = player
        self.move_calculator = move_calculator

    def get_tile(self) -> TileBase:
        return TrapTile(self.move_calculator, self.player, self.trap_damage, self.on_tile_entity)