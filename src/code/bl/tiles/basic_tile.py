from code.bl.tiles.abstract.tile_base import TileBase
from code.bl.util.move import Move
from code.bl.util.point import Point


class BasicTile(TileBase):
    def get_after_move_point(self, tile_point: Point, move_to_tile: Move) -> Point:
        return tile_point