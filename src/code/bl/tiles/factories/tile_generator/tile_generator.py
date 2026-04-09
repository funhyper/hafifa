from code.bl.tiles.abstract.tile_base import TileBase
from code.bl.tiles.abstract.tile_factory_base import TileFactoryBase
from code.bl.util.random_provider import RandomProvider


class TileGenerator(TileFactoryBase):
    def __init__(self, random_provider: RandomProvider, tile_factories: list[TileFactoryBase]):
        self.tile_factories = tile_factories
        self.random_provider = random_provider

    def get_tile(self) -> TileBase:
        factory_index = self.random_provider.get_random_number(0, len(self.tile_factories))
        factory = self.tile_factories[factory_index]
        return factory.get_tile()