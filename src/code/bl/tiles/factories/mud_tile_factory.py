from code.bl.entities.abstract.monster_base import MonsterBase
from code.bl.tiles.abstract.tile_base import TileBase
from code.bl.tiles.abstract.tile_factory_base import TileFactoryBase
from code.bl.tiles.mud_tile import MudTile
from code.bl.util.move_calculator import MoveCalculator


class MudTileFactory(TileFactoryBase):
    def __init__(self, move_calculator: MoveCalculator, moves_stuck: int,
                 on_tile_entity: MonsterBase = None):
        self.on_tile_entity = on_tile_entity
        self.moves_stuck = moves_stuck
        self.move_calculator = move_calculator

    def get_tile(self) -> TileBase:
        return MudTile(self.move_calculator, self.moves_stuck, self.on_tile_entity)