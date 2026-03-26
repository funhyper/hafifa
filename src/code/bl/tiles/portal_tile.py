from code.bl.tiles.abstract.tile_base import TileBase
from code.bl.util.move import Move
from code.bl.util.point import Point
from code.bl.util.random_provider import RandomProvider


class PortalTile(TileBase):
    def __init__(self, random_provider: RandomProvider, entity: EntityBase = None):
        super().__init__(entity)
        self.random_provider = random_provider

    def get_point_after_move(self, player_point: Point, move: Move) -> Point:
        return self.random_provider.get_random_board_point()