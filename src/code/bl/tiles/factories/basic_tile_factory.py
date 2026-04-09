from code.bl.entities.abstract.monster_base import MonsterBase
from code.bl.tiles.abstract.tile_base import TileBase
from code.bl.tiles.abstract.tile_factory_base import TileFactoryBase
from code.bl.tiles.basic_tile import BasicTile
from code.bl.util.move_calculator import MoveCalculator


class BasicTileFactory(TileFactoryBase):
    def __init__(self, move_calculator: MoveCalculator, on_tile_entity: MonsterBase = None):
        self.on_tile_entity = on_tile_entity
        self.move_calculator = move_calculator

    def get_tile(self) -> TileBase:
        return BasicTile(self.move_calculator, self.on_tile_entity)