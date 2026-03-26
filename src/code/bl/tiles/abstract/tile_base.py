from abc import ABC, abstractmethod

from code.bl.util.move import Move
from code.bl.util.point import Point


class TileBase(ABC):
    def __init__(self, entity: EntityBase=None):
        self.entity = entity

    @abstractmethod
    def get_point_after_move(self, player_point: Point, move: Move) -> Point:
        raise NotImplementedError