from abc import ABC, abstractmethod

from code.bl.util.move import Move
from code.bl.util.point import Point


class TileBase(ABC):
    def __init__(self, entity: EntityBase = None):
        self.entity = entity

    @abstractmethod
    def get_after_move_point(self, tile_point: Point, move_to_tile: Move) -> Point:
        raise NotImplementedError