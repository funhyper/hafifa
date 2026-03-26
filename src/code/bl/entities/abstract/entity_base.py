from abc import ABC

from code.excpetions.entity_exceptions import DamageDeadEntityException


class EntityBase(ABC):
    def __init__(self, health = 100):
        self.health = health

    def damage_entity(self, damage: int) -> None:
        if self.is_dead():
            raise DamageDeadEntityException()
        self.health -= damage

    def is_dead(self) -> bool:
        return self.health <= 0