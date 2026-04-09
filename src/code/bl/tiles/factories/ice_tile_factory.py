from code.bl.entities.abstract.monster_base import MonsterBase
from code.bl.tiles.abstract.tile_base import TileBase
from code.bl.tiles.abstract.tile_factory_base import TileFactoryBase
from code.bl.tiles.ice_tile import IceTile
from code.bl.util.move_calculator import MoveCalculator


class IceTileFactory(TileFactoryBase):

    def __init__(self, move_calculator: MoveCalculator, skipped_tiles_count: int,
                 on_tile_entity: MonsterBase = None):
        self.skipped_tiles_count = skipped_tiles_count
        self.on_tile_entity = on_tile_entity
        self.move_calculator = move_calculator

    def get_tile(self) -> TileBase:
        return IceTile(self.move_calculator, self. skipped_tiles_count, self.on_tile_entity)