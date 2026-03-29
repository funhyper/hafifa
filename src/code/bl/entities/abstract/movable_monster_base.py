from abc import abstractmethod, ABC

from code.bl.entities.abstract.monster_base import MonsterBase
from code.bl.util.move import Move
from code.bl.util.point import Point


class MovableMonsterBase(MonsterBase, ABC):
    @abstractmethod
    def get_next_move(self, current_location: Point) ->     Move:
        raise NotImplementedError