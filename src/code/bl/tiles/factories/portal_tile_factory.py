from code.bl.entities.abstract.monster_base import MonsterBase
from code.bl.tiles.abstract.tile_base import TileBase
from code.bl.tiles.abstract.tile_factory_base import TileFactoryBase
from code.bl.tiles.portal_tile import PortalTile
from code.bl.util.random_provider import RandomProvider


class PortalTileFactory(TileFactoryBase):
    def __init__(self, random_provider: RandomProvider, on_tile_entity: MonsterBase = None):
        self.on_tile_entity = on_tile_entity
        self.random_provider = random_provider

    def get_tile(self) -> TileBase:
        return PortalTile(self.random_provider, self.on_tile_entity)