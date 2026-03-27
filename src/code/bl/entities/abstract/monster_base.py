from abc import ABC, abstractmethod

from code.bl.entities.entity import Entity


class MonsterBase(Entity, ABC):
    @abstractmethod
    def get_dealt_damage(self, entity: Entity) -> int:
        raise NotImplementedError