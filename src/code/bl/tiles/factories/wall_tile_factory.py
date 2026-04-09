from code.bl.tiles.abstract.tile_base import TileBase
from code.bl.tiles.abstract.tile_factory_base import TileFactoryBase
from code.bl.tiles.wall_tile import WallTile


class WallTileFactory(TileFactoryBase):
    def get_tile(self) -> TileBase:
        return WallTile()