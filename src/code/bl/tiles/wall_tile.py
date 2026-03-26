from code.bl.tiles.abstract.tile_base import TileBase
from code.bl.util.move import Move
from code.bl.util.point import Point


class WallTile(TileBase):
    def get_point_after_move(self, player_point: Point, move: Move) -> Point:
        return player_point