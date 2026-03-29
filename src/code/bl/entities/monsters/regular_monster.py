from code.bl.entities.abstract.monster_base import MonsterBase
from code.bl.entities.entity import Entity


class RegularMonster(MonsterBase):
    def __init__(self, attack_damage: int, health: int = 100):
        super().__init__(health)
        self.attack_damage = attack_damage

    def get_dealt_damage(self, entity: Entity) -> int:
        return self.attack_damage
