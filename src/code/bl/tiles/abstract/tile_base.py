from abc import ABC, abstractmethod

from code.bl.entities.abstract.monster_base import MonsterBase
from code.bl.util.move import Move
from code.bl.util.point import Point


class TileBase(ABC):
    def __init__(self, on_tile_entity: MonsterBase = None):
        self.on_tile_entity = on_tile_entity

    @abstractmethod
    def get_point_after_move(self, player_point: Point, move: Move) -> Point:
        raise NotImplementedError
